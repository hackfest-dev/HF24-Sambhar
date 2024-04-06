import numpy as np
import pandas as pd
import mysql.connector
from xgboost import XGBRegressor

class dt_regressor_sambhar:
    def __init__(self):
        self.host1 = "localhost"
        self.user1 = "root"
        self.password1 = ""
        self.database1 = "Inventory_management"

        self.connection = mysql.connector.connect(
            host=self.host1,
            user=self.user1,
            password=self.password1,
            database=self.database1
        )

        self.cursor = self.connection.cursor()


        self.cursor.execute("SELECT item_id, unit, price_per_unit, SUM(quantity) AS total_quantity FROM transaction GROUP BY item_id, unit, price_per_unit")
        self.number_of_sales = self.cursor.fetchall()

    def preprocess_data(self):
        # Convert fetched data to a DataFrame
        dt.df = pd.DataFrame(self.number_of_sales, columns=['item_id', 'unit', 'price_per_unit', 'total_quantity'])

        # Data Cleaning: Handle missing values
        dt.df.dropna(inplace=True)

        # Data Cleaning: Handle outliers (if needed)
        # For example, remove rows with price_per_unit that are greater than a certain threshold

    def predict(self):
        self.preprocess_data()  # Call preprocess_data method
        self.X = dt.df[['price_per_unit', 'total_quantity']].values
        self.y = dt.df['total_quantity'].astype(int)

    def predictions(self, max_leaf_nodes, user_input):
        model = XGBRegressor(n_estimators=100, max_depth=3, tree_method='hist', device='cuda', sampling_method='gradient_based', learning_rate=0.1, objective='reg:squarederror')
        model.fit(self.X, self.y)
        self.prediction = model.predict([user_input])
        return self.prediction[0]

if __name__ == '__main__':
    dt = dt_regressor_sambhar()
    dt.predict()
    ip = int(input("Enter the budget"))

    for max_nodes in [2]:
        prediction = dt.predictions(max_nodes, ip)

    total_prediction = dt.df['price_per_unit'].sum() * (int(ip) / prediction)

    dt.df['investment_ratio'] = (dt.df['price_per_unit'] / total_prediction) * int(ip)

    total_ratio = dt.df['investment_ratio'].sum()

