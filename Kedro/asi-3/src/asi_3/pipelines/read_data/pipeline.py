from kedro.pipeline import Pipeline, node, pipeline

from .nodes import download_data_from_url, save_data_to_file, read_data, read_file

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=read_data,
                inputs=["data_url"],
                outputs=None,
                name="all_data"
            )
        ]
    ) 

