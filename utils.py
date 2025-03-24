# utils.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_duplicates_bar(train_duplicates, test_duplicates, overlap_df):
    plt.figure(figsize=(8, 5))
    sns.barplot(
        x=["Train Duplicates", "Test Duplicates", "Train-Test Overlap"],
        y=[len(train_duplicates), len(test_duplicates), len(overlap_df)],
        palette=["skyblue", "salmon", "orange"]
    )
    plt.title("Duplicate and Overlap Counts in Dataset")
    plt.ylabel("Number of Entries")
    plt.tight_layout()
    plt.show()
