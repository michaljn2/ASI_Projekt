from autogluon.tabular import TabularDataset

def read_data(data_url: str) -> TabularDataset:
    all_data = TabularDataset(f'{data_url}weatherAUS.csv')
    return all_data