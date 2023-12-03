"""
This is a boilerplate pipeline 'load_data'
generated using Kedro 0.18.14
"""

from autogluon.tabular import TabularDataset

def load_data(weatherAUS):
    # plain_data = catalog.load("weatherAUS")
    all_data = TabularDataset(weatherAUS)
    return all_data