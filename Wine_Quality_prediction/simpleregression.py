import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import tree, linear_model

class Wine_Data:
    def __init__(self):
        self.data = pd.read_csv('data/wineQualityReds.csv')

    def data_stats(self):
        #summary of data
        print(self.data.describe().transpose)

        #check for missing values
        print((self.data.isnull().sum()/len(self.data)).sort_values(ascending= False)) #0.0 they suggest 0% data are missing in that columnname

    def model_regression(self):
        df = self.data

        cols = df.columns
        features = cols[1:-1]
        target = cols[-1]

        X = self.data[features]
        y = self.data[target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

        model = linear_model.LinearRegression()
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        print("Accuracy score of model: ", accuracy)

        self.predict = model.predict(X_test)
        self.predict_full = model.predict(X)
        print(self.predict)

        #Error calculation - Root mean Squared error, Mean Absolute error
        rmse = mean_squared_error(self.predict, y_test) * 100
        mae = mean_absolute_error(self.predict, y_test) * 100

        print('RMSE: {}     MAE: {}'.format(rmse, mae))

    def final_dataset(self):
        df = self.data
        df['predictions'] = pd.Series(self.predict_full)
        df.to_csv('./data/prediction_results.csv')
        print(df.head())


wine = Wine_Data()
print(wine.data.head(5))
wine.data_stats()
wine.model_regression()
wine.final_dataset()
