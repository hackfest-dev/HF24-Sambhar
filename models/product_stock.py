import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

class product_stock:
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

    def plot1(self):
        self.cursor.execute("SELECT finished_prod_id, SUM(quantity) FROM produces GROUP BY finished_prod_id")
        results = self.cursor.fetchall()
        df = pd.DataFrame(results, columns=["finished_prod_id", "total_quantity"])

        fig, ax = plt.subplots(figsize=(10, 6))

        raw_materials_query = "SELECT finished_prod_id, raw_material_id, SUM(quantity) FROM produces GROUP BY finished_prod_id, raw_material_id"
        self.cursor.execute(raw_materials_query)
        raw_materials_results = self.cursor.fetchall()
        raw_materials_df = pd.DataFrame(raw_materials_results, columns=["finished_prod_id", "raw_material_id", "quantity"])

        unique_finished_prod_ids = df["finished_prod_id"].tolist()
        unique_raw_material_ids = raw_materials_df["raw_material_id"].unique()

        width = 0.2
        x = np.arange(len(unique_finished_prod_ids))

        for i, raw_material_id in enumerate(unique_raw_material_ids):
            quantities = []
            for finished_prod_id in unique_finished_prod_ids:
                quantity = raw_materials_df[(raw_materials_df["finished_prod_id"] == finished_prod_id) & (raw_materials_df["raw_material_id"] == raw_material_id)]["quantity"].values
                quantities.append(quantity[0] if quantity.size > 0 else 0)
            ax.bar(x + (i - 1) * width/6, quantities, width, label=f'Raw Material ID: {raw_material_id}')

        ax.set_xlabel('Finished Product ID')
        ax.set_ylabel('Quantity')
        ax.set_title('Raw Material Quantity by Finished Product')
        ax.set_xticks(x)
        ax.set_xticklabels(unique_finished_prod_ids, rotation=45, ha='right')
        ax.legend()

        # plt.show()
        plt.savefig('pie1_chart.png', dpi = 130) 



if __name__ == '__main__':
    connected1 = product_stock()
    connected1.plot1()