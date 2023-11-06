import read_data
import transform_data
import train_model

import wandb
from wandb.sklearn import plot_precision_recall, plot_feature_importances
from wandb.sklearn import plot_class_proportions, plot_learning_curve, plot_roc


def main():
    url = "https://raw.githubusercontent.com/michaljn2/ASI_Projekt/main/weatherAUS.csv"
    csv_path = "data/weatherAUS.csv"

    # read_data.read_data(url, csv_path)
    df = read_data.read_file(csv_path)

    X_train, X_val, X_test, y_train, y_val, y_test = transform_data.transform(df)
    model = train_model.train_model(X_train, y_train)
    train_model.evaluate_model(model, X_train, X_test, y_train, y_test)

    y_pred = model.predict(X_test)
    y_probas = model.predict_proba(X_test)

    wandb.init(project="ASI_weather", config=model.get_params())

    wandb.config.update(
        {"test_size": 0.15, "train_len": len(X_train), "test_len": len(X_test)}
    )

    plot_class_proportions(y_train, y_test, labels=df.columns)
    plot_learning_curve(model, X_train, y_train)
    plot_roc(y_test, y_probas, labels=df.columns)
    plot_precision_recall(y_test, y_probas, labels=df.columns)
    plot_feature_importances(model)

    wandb.finish()


if __name__ == "__main__":
    main()
