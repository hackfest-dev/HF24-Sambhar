import numpy as np
import pandas as pd
import mysql.connector
from sklearn.tree import DecisionTreeRegressor

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
        
    def predict(self):

        dt.df = pd.DataFrame(self.number_of_sales, columns=['item_id', 'unit', 'price_per_unit', 'total_quantity'])
        self.feature_names = dt.df['price_per_unit'].tolist()
        self.y = dt.df['total_quantity']


    def predictions(self, max_leaf_nodes, user_input):
        X = np.array(self.feature_names).reshape(-1, 1)
        model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
        model.fit(X, self.y)
        depth = model.get_depth()

        # print(depth)
        self.prediction = model.predict([[user_input]])
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

    dt.df['investment_ratio'] = dt.df['investment_ratio']/total_ratio

    dt.df['investment_ratio'] = dt.df['investment_ratio'] * ip

    print(dt.df[['item_id', 'investment_ratio']])