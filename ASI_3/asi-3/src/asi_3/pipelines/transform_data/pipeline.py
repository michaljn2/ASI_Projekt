from kedro.pipeline import node, Pipeline
from .nodes import (  # Replace 'your_module' with the actual module where your functions are defined.
    transform,
    drop_rows_without_target,
    transform_categorical_features,
    transform_numerical_features,
    transform_date_column,
    transform_no_yes,
    one_hot_encoding,
    extract_features,
    extract_target,
    split_train_test,
    scale_features,
)

def create_pipeline():
    return Pipeline(
        [
            node(func=drop_rows_without_target, inputs="your_input_data", outputs="data_cleaned", name="drop_rows_without_target"),
            node(func=transform_categorical_features, inputs="data_cleaned", outputs="categorical_transformed", name="transform_categorical_features"),
            node(func=transform_numerical_features, inputs="categorical_transformed", outputs="numerical_transformed", name="transform_numerical_features"),
            node(func=transform_date_column, inputs="numerical_transformed", outputs="date_transformed", name="transform_date_column"),
            node(func=transform_no_yes, inputs="date_transformed", outputs="binary_transformed", name="transform_no_yes"),
            node(func=one_hot_encoding, inputs="binary_transformed", outputs="one_hot_encoded", name="one_hot_encoding"),
            node(func=extract_features, inputs="one_hot_encoded", outputs="X", name="extract_features"),
            node(func=extract_target, inputs="one_hot_encoded", outputs="y", name="extract_target"),
            node(func=split_train_test, inputs=["X", "y"], outputs=["X_train", "X_test", "y_train", "y_test", "X_val", "y_val"], name="split_train_test"),
            node(func=scale_features, inputs=["X_train", "X_val", "X_test"], outputs=["X_train_scaled", "X_val_scaled", "X_test_scaled"], name="scale_features"),
        ]
    )
