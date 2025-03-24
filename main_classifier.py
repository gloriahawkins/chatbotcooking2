# main_classifier.py
from data_loader import load_datasets
from data_cleaner import clean_datasets
from analysis import analyze_distributions, plot_distributions, generate_wordcloud
from model_trainer import train_and_evaluate_models
from utils import plot_duplicates_bar

# === 1. Load Datasets ===
train_df, test_df = load_datasets("training_cooking_classification.csv", "testing_cooking_classification.csv")
generate_wordcloud(train_df, "cooking")
generate_wordcloud(train_df, "non-cooking")
# === 2. Clean Datasets (remove duplicates and overlaps) ===
train_df, overlap_df, train_duplicates, test_duplicates = clean_datasets(train_df, test_df)

# === 3. Plot duplicate and overlap counts ===
plot_duplicates_bar(train_duplicates, test_duplicates, overlap_df)

# === 4. Analyze Class Distributions ===
analyze_distributions(train_df, test_df)

# === 5. Plot Class Distribution Charts ===
plot_distributions(train_df, test_df)


# === 6. Train and Evaluate Models ===
train_and_evaluate_models(train_df, test_df)
