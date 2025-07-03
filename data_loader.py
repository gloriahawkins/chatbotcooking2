# data_loader.py
import pandas as pd

#basic function to load in the datasets
def load_datasets(train_path, test_path):
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    print("Datasets loaded successfully.")
    return train_df, test_df
