import numpy as np
import pandas as pd
import mysql.connector
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Connect to the MySQL database
host1 = "localhost"
user1 = "root"
password1 = "Vignesh@ara"
database1 = "Inventory_management"

connection = mysql.connector.connect(
    host=host1,
    user=user1,
    password=password1,
    database=database1
)

cursor = connection.cursor()

# Execute SQL query and fetch results
cursor.execute("SELECT item_id, unit, price_per_unit, SUM(quantity) AS total_quantity FROM TRANSACTION GROUP BY item_id")
number_of_sales = cursor.fetchall()

# Convert to DataFrame
df = pd.DataFrame(number_of_sales, columns=['item_id', 'unit', 'price_per_unit', 'total_quantity'])

# Prepare features and target variable
X = df[['total_quantity']]
y = df['price_per_unit']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Gradient Boosting Regressor
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Fit the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Example prediction
total_budget = float(input("Enter the total budget: "))
predicted_prices = model.predict([[total_budget]])

# Retrieve item_id corresponding to the predicted prices
item_ids = df['item_id'].values
predicted_prices_with_item_ids = list(zip(item_ids, predicted_prices))

print("Predicted prices for each item based on total budget:")
for item_id, predicted_price in predicted_prices_with_item_ids:
    print(f"Item ID: {item_id}, Predicted Price: {predicted_price}")