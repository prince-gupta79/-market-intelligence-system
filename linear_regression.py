# it is almost like predicting tommorow
# by this formual
# y = mx + b

import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


symbol = "GLD"
df = yf.download(symbol, period = "30d")
df['Day_Number'] = np.arange(len(df)) 

# reshaping for the model
# scikit-learn expects x to be a 2D array
x = df[['Day_Number']].values
y = df['Close'].squeeze().values

model = LinearRegression()
model.fit(x,y)

# predicting the future (next 5-D)
last_day = len(df)
future_days = np.array([[last_day + i] for i in range(1, 6)])
predictions = model.predict(future_days)

print(f">>> 5-D PREDICTION >>>")
for i, price in enumerate(predictions):
    print(f"Day {i+1}: ${price:.2f}")

r_squared = model.score(x,y)
print(f"Model Confidence (R-Squared) : {r_squared:.4f}")

# the visiuals
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Actual Price')
plt.plot(x, model.predict(x), color='red', label='Trend Line(Prediction)')
plt.title(f"{symbol} Price Prediction Model")
plt.legend()
plt.show()