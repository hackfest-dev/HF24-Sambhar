import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import mysql.connector
# Load your historical data
host1 = "localhost"
user1 = "root"
password1 = ""
database1 = "Inventory_management"
connection = mysql.connector.connect(
    host=host1,
    user=user1,
    password=password1,
    database=database1
)

cursor = connection.cursor()

cursor.execute("SELECT material_id, mat_date, mrp FROM material_history")
x = cursor.fetchall()

df = pd.DataFrame(x, columns=["material_id", "mat_date", "mrp"])

# Aggregate material_id data by date
group_data = df.groupby(['mat_date', 'material_id']).mean().reset_index()

# Pivot the table to have date as index and material_id as columns
pivot_data = group_data.pivot(index='mat_date', columns='material_id', values='mrp')

# Fill missing values with forward fill
pivot_data = pivot_data.ffill()

# Set frequency of the index
pivot_data.index = pd.to_datetime(pivot_data.index)
pivot_data.index.freq = pd.infer_freq(pivot_data.index)

# Split the data into training and validation sets
train_data = pivot_data.iloc[:-1]  # Use the last month as validation set
valid_data = pivot_data.iloc[-1:]

# Fit SARIMAX model to the training data for each material_id
predictions = {}
for col in train_data.columns:
    model = SARIMAX(train_data[col], order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
    results = model.fit()
    forecast = results.forecast(steps=1)
    predictions[col] = forecast[0]

# Print the predicted prices for the next month
print("Predicted Prices for Next Month:")
for material_id, price in predictions.items():
    print(f"{material_id}: {price}")

# Plot the predicted prices
plt.figure(figsize=(10, 6))
for material_id, price in predictions.items():
    plt.plot(valid_data.index, [price] * len(valid_data), label=material_id)

plt.title('Predicted Prices for Next Month')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
