# random forest creates hundreds of decisions tress to predict real chaotic market
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# feccting deep data
df = yf.download("GLD", period = "1y")

# expert fetaures enginnering
df['Day_Number'] = range(len(df))
df['MA_5'] = df['Close'].rolling(5).mean()
df['MA_20'] = df['Close'].rolling(20).mean()
df['Volume_Change'] = df['Volume'].pct_change()

df = df.dropna()

# degining features(x) & target(y)
features = ['Day_Number', 'Volume', 'MA_5', 'MA_20', 'Volume_Change']
X = df[features].values
y = df['Close'].squeeze().values

# split data [train on 80%, test on 20%]
# this prevents "cheating" so we see how it works on new data
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# building & traning yhe forest
forest = RandomForestRegressor(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)

# scoring the forest
score = forest.score(X_test, y_test)
print((f"RANDOM FOREST SCORE:{score:.4f}"))

# importance: whgich forest did the forest care about nost?
importance = forest.feature_importances_
for i, feature in enumerate(features):
    print(f"Impact of {feature}: {importance[i]:.4f}")

r_squared = forest.score(X,y)
print(f"Model Confidence (R-Squared) : {r_squared:.4f}")
