from autogluon.tabular import TabularPredictor


def train_model(label: str, train_data) -> TabularPredictor:
    return TabularPredictor(label=label).fit(train_data)