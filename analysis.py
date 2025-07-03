# analysis.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#analyze the ML dataset for classification

def analyze_distributions(train_df, test_df):
    print("\n=== Class Distribution Analysis ===")

    print("\nTraining Dataset Class Distribution:")
    train_counts = train_df["label"].value_counts()
    train_percentages = train_df["label"].value_counts(normalize=True) * 100
    print(train_counts)
    print("\nTraining Dataset Class Distribution (Percentage):")
    print(train_percentages.round(2))

    print("\nTest Dataset Class Distribution:")
    test_counts = test_df["label"].value_counts()
    test_percentages = test_df["label"].value_counts(normalize=True) * 100
    print(test_counts)
    print("\nTest Dataset Class Distribution (Percentage):")
    print(test_percentages.round(2))

def plot_distributions(train_df, test_df):
    train_counts = train_df["label"].value_counts()
    test_counts = test_df["label"].value_counts()

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    train_counts.plot(kind="bar", color=["skyblue", "salmon"])
    plt.title("Training Set Class Distribution")
    plt.xlabel("Class")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    test_counts.plot(kind="bar", color=["skyblue", "salmon"])
    plt.title("Test Set Class Distribution")
    plt.xlabel("Class")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

def generate_wordcloud(df, label):
    subset = df[df['label'] == label]
    text = " ".join(subset['text'].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for '{label}' Class")
    plt.tight_layout()
    plt
