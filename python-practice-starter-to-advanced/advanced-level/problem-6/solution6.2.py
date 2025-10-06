import pandas as pd

df = pd.read_csv('users.csv')
top_users = df.sort_values(by='score', ascending=False).head(5)

print(top_users)