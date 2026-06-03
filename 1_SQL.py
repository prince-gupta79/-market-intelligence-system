# this code will be used directly for the price re;ated 
# for NVDA with writing the whole scripts of codes in python

import sqlite3

conn  = sqlite3.connect('market_intelligence.db')

# finding the average price of nvidia in our logs
query = "SELECT AVG(price) FROM market_data WHERE ticker ='NVDA'"

results = conn.execute(query).fetchone()
print(f"The average Logged Price is: €{results[0]:.2f}")

conn.close()