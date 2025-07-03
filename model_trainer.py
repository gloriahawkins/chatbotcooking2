# model_trainer.py
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

#train and eval different models
def train_and_evaluate_models(train_df, test_df):
    X_train = train_df["text"]
    y_train = train_df["label"]
    X_test = test_df["text"]
    y_test = test_df["label"]

    models = {
        "LogisticRegression": LogisticRegression(max_iter=500),
        "MultinomialNB": MultinomialNB(),
        "LinearSVC": LinearSVC(),
        "RandomForest": RandomForestClassifier(n_estimators=100),
        "GradientBoosting": GradientBoostingClassifier(),
        "KNeighbors": KNeighborsClassifier(),
        "DecisionTree": DecisionTreeClassifier(),
        "RidgeClassifier": RidgeClassifier()
    }

    best_model = None
    best_score = 0
    best_model_name = ""

    for name, model in models.items():
        print(f"\n===== {name} =====")
        pipeline = Pipeline([
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english")),
            ("clf", model)
        ])

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        

        acc = accuracy_score(y_test, y_pred)
        print(f" Accuracy on test set: {acc:.2%}")
        print(classification_report(y_test, y_pred))
        
          # Generate and plot confusion matrix
        cm = confusion_matrix(y_test, y_pred, labels=["cooking", "non-cooking"])
    
        plt.figure(figsize=(5, 4))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
                    xticklabels=["cooking", "non-cooking"],
                    yticklabels=["cooking", "non-cooking"])
        plt.title(f"Confusion Matrix - {name}")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.tight_layout()
        plt.show()


        if acc > best_score:
            best_score = acc
            best_model = pipeline
            best_model_name = name

    joblib.dump(best_model, "topic_classifier_final.pkl")
    print(f"\n Best model: {best_model_name} with accuracy {best_score:.2%}")
    print(" Saved as: topic_classifier_final.pkl")
