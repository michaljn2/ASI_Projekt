import read_data as rd
import transform_data
import train_model


def main():
    url = 'https://raw.githubusercontent.com/michaljn2/ASI_Projekt/main/weatherAUS.csv'
    rd.read_data(url)
    X_train, X_test, y_train, y_test = transform_data.transform()

    model = train_model.train_model(X_train, y_train)
    train_model.evaluate_model(model, X_train, X_test, y_train, y_test)



if __name__ == '__main__':
    main()
