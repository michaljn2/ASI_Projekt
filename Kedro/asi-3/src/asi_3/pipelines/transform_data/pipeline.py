from kedro.pipeline import node, Pipeline
from .nodes import (  # Replace 'your_module' with the actual module where your functions are defined.
    transform_data,
)


def create_pipeline():
    return Pipeline(
        [
            node(
                func=transform_data,
                inputs=["all_data", "label"],
                outputs=["train_data", "test_data"],
                name="transform_data",
            )
        ]
    )
