from autogluon.tabular import TabularDataset
from sklearn.model_selection import train_test_split
import numpy

def transform_data(all_data: TabularDataset, label: str):
    all_data.dropna(axis=0, subset=[label], inplace=True)
    train_data, test_data = train_test_split(all_data, test_size=0.2, random_state=100)
    return train_data, test_data