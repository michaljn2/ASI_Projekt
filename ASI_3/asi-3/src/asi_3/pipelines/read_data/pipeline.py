from kedro.pipeline import Pipeline, node, pipeline

from .nodes import download_data_from_url, save_data_to_file, read_data, read_file

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=read_data,
                inputs=["url", "path"],
                outputs=None,
                name="read_data"
            ),
            node(
                func=read_file,
                inputs=["path"],
                outputs=["df"],
                name="read_file"
            )
        ]
    ) 

