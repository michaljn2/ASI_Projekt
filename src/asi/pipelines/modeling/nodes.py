"""
This is a boilerplate pipeline 'modeling'
generated using Kedro 0.18.14
"""
from autogluon.tabular import TabularDataset, TabularPredictor

def train_model(train_data):
    label="RainTomorrow"
    predictor = TabularPredictor(label=label).fit(train_data)
    return predictor

def evaluate_model(predictor, test_data):
    predictor.evaluate(test_data, silent=True)