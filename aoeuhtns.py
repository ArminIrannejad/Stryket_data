import pandas as pd
import numpy as np
import requests

def get_data():
    response = requests.get("https://tipsxtra.se/statistics/exportcsv/details/1").json()['csv']
    with open('raw_data.csv', 'w') as file:
        file.write(response)

    
def main():
    get_data()
    df = pd.read_csv('raw_data.csv', delimiter=';')
    print(df.head())

if __name__ == "__main__":
    main()
