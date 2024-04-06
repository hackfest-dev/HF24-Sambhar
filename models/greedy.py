import numpy as np
import pandas as pd
import mysql.connector

class InvestmentAllocator:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "Inventory_management"

        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT item_id, unit, price_per_unit, SUM(quantity) AS total_quantity FROM transaction GROUP BY item_id, unit, price_per_unit")
        self.number_of_sales = self.cursor.fetchall()

    def allocate_investment(self, budget):
        df = pd.DataFrame(self.number_of_sales, columns=['item_id', 'unit', 'price_per_unit', 'total_quantity'])

        # Calculate the profit for each item based on historical sales and price_per_unit
        df['profit_per_unit'] = df['price_per_unit'] * df['total_quantity']

        # Sort the items by profit_per_unit in descending order
        df = df.sort_values(by='profit_per_unit', ascending=False)

        # Allocate budget based on historical profit contribution
        df['investment_ratio'] = (df['profit_per_unit'] / df['profit_per_unit'].sum()) * budget

        return df[['item_id', 'investment_ratio']]

if __name__ == '__main__':
    allocator = InvestmentAllocator()
    budget = int(input("Enter the budget: "))
    investment_allocation = allocator.allocate_investment(budget)
    print("Predicted investment ratios:")
    print(investment_allocation)
