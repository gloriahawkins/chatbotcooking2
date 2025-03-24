# data_cleaner.py
def clean_datasets(train_df, test_df):
    # Check for internal duplicates
    train_duplicates = train_df[train_df.duplicated(subset=["text"], keep=False)]
    test_duplicates = test_df[test_df.duplicated(subset=["text"], keep=False)]

    # Check for overlap between train and test
    overlap_df = train_df.merge(test_df, on="text", how="inner")

    # Remove overlapping and duplicate rows from training set
    train_df_cleaned = train_df[~train_df["text"].isin(overlap_df["text"])]
    train_df_cleaned = train_df_cleaned.drop_duplicates(subset=["text"], keep="first")

    print("Training set cleaned (duplicates & overlaps removed).")
    return train_df_cleaned, overlap_df, train_duplicates, test_duplicates
