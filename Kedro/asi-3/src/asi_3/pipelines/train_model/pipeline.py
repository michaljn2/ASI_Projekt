from kedro.pipeline import Pipeline, node, pipeline

from .nodes import train_model, evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_model,
                inputs=["label", "train_data"],
                outputs=["predictor"],
                name="train_model",
            )
        ]
    )