import pandas as pd
from sklearn.impute import SimpleImputer


def load_dataset(path):
    return pd.read_csv(path)


def preprocess_data(df):
    imputer = SimpleImputer(strategy='median')
    return df
