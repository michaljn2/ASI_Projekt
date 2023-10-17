import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def transform(df: pd.DataFrame):
    drop_rows_without_target(df)
    transform_categorical_features(df)
    transform_numerical_features(df)
    transform_date_column(df)
    transform_no_yes(df)
    df = one_hot_encoding(df)
    X = extract_features(df)
    y = extract_target(df)
    X_train, X_test, y_train, y_test, X_val, y_val = split_train_test(X, y)
    X_train, X_val, X_test = scale_features(X_train, X_val, X_test)

    return X_train, X_val, X_test, y_train, y_val, y_test


def drop_rows_without_target(df: pd.DataFrame):
    df.dropna(axis=0, subset=['RainTomorrow'], inplace=True)


def transform_categorical_features(df: pd.DataFrame):
    categorical = [var for var in df.columns if df[var].dtype == 'O']

    for col in categorical:
        col_mode = df[col].mode()[0]
        df[col].fillna(col_mode, inplace=True)


def transform_numerical_features(df: pd.DataFrame):
    numerical = [var for var in df.columns if df[var].dtype != 'O']

    for col in numerical:
        col_median = df[col].median()
        df[col].fillna(col_median, inplace=True)


def transform_date_column(df: pd.DataFrame):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df.drop('Date', axis=1, inplace=True)


def transform_no_yes(df: pd.DataFrame):
    df['RainToday'].replace({'No': 0, 'Yes': 1}, inplace=True)
    df['RainTomorrow'].replace({'No': 0, 'Yes': 1}, inplace=True)


def one_hot_encoding(df: pd.DataFrame):
    df = pd.get_dummies(data=df, columns=['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm'])

    return df


def extract_features(df: pd.DataFrame):
    X = df.drop(['RainTomorrow'], axis=1)

    return X


def extract_target(df: pd.DataFrame):
    y = df['RainTomorrow']

    return y


def split_train_test(X, y):
    # TODO - Do przetestowania czy train jest jednakowy. Oddzielić train od test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.15, random_state=42)

    return X_train, X_test, y_train, y_test, X_val, y_val


def scale_features(X_train, X_val, X_test):
    # TODO -  scalować validacyjne
    cols = X_train.columns

    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)

    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    X_train = pd.DataFrame(X_train, columns=[cols])
    X_val = pd.DataFrame(X_val, columns=[cols])
    X_test = pd.DataFrame(X_test, columns=[cols])

    return X_train, X_val, X_test
