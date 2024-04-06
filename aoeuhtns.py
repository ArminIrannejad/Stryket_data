import pandas as pd
import numpy as np
import requests

response = requests.get("https://tipsxtra.se/statistics/exportcsv/details/1").json()['csv']

with open('raw_data.csv', 'w') as file:
    file.write(response)

df = pd.read_csv('raw_data.csv', delimiter=';')
print(df.head())

