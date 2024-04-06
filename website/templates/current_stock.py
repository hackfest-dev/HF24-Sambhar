import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import mysql.connector

class current_stock:
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
        plt.style.use('_mpl-gallery-nogrid')
        self.cursor.execute("SELECT item_id, item_name, current_stock FROM inventory")
        x = self.cursor.fetchall()
        df = pd.DataFrame(x, columns=["item_id", "item_name", "current_stock"])
        values = df["current_stock"]
        labels = df["item_id"].tolist()
        handles = []
        colors = plt.get_cmap('Blues')(np.linspace(0.1, 1.0, len(values)))
        for i, label in enumerate(labels):
            handle = mpatches.Patch(color=colors[i], label=label)
            handles.append(handle)

        fig, ax = plt.subplots(figsize=(3,3))
        ax.set_aspect('equal')
        ax.pie(values, colors=colors,radius=1,wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
        
        plt.title("CURRENT STOCK QUANTITY")
        ax.legend(handles=handles, labels=labels, loc='upper right', fontsize = 'small')
        plt.show()
        plt.savefig('pie_chart.png') 

if __name__ == '__main__':
    connected = current_stock()
    connected.plot1()

