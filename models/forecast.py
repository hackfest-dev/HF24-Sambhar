import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import mysql.connector
# Load your historical data
# Assuming 'date' is the date column and 'price' is the raw material price column
# Replace 'your_data.csv' with the actual filename or database query


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

cursor.execute("SELECT material_id, mat_date FROM material_history")
x = cursor.fetchall()

df = pd.DataFrame(x, columns=["material_id", "mat_date"])

# Convert 'date' column to datetime format and set it as index
df['date'] = pd.to_datetime(df["mat_date"])
df.set_index('date', inplace=True)
df.drop(columns="mat_date", inplace=True)
# Perform any necessary data preprocessing, e.g., filling missing values, resampling
print(df)
# Visualize the time series
plt.figure(figsize=(10, 6))
plt.plot(df.index.tolist(), df['material_id'].values.tolist(), label='Material ID')
plt.title('Raw Material Price Time Series')
plt.xlabel('Date')
plt.ylabel('Material ID')
plt.show()

# Decompose the time series to identify trends and seasonality
# decomposition = seasonal_decompose(data, model='additive')
# decomposition.plot()
# plt.show()

# Stationarity check
# You can use statistical tests like ADF or KPSS, or visualize ACF and PACF plots
# If non-stationary, perform differencing or other transformations

# SARIMA model parameters selection using ACF and PACF plots
# plot_acf(data, lags=20)
# plot_pacf(data, lags=20)
# plt.show()

# Define SARIMA model parameters
p = 1  # Autoregressive order
d = 1  # Differencing order
q = 1  # Moving average order
P = 1  # Seasonal autoregressive order
D = 1  # Seasonal differencing order
Q = 1  # Seasonal moving average order
m = 12  # Seasonal period (assuming monthly data)

# Split the data into training and validation sets
train_data = df.iloc[:-12]  # Use the last 12 months as validation set
valid_data = df.iloc[-12:]

# Fit SARIMA model to the training data
model = SARIMAX(train_data, order=(p, d, q), seasonal_order=(P, D, Q, m))
results = model.fit()

# Make predictions for the next 3 months
forecast = results.forecast(steps=3)

# Print the forecasted prices
print("Forecasted Prices:")
print(forecast)

# Visualize the forecast
plt.figure(figsize=(10, 6))
plt.plot(train_data.index, train_data, label='Training Data')
plt.plot(valid_data.index, valid_data, label='Validation Data')
plt.plot(forecast.index, forecast, label='Forecast', color='red')
plt.title('Raw Material Price Forecast')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
