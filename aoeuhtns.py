import pandas as pd
import numpy as np
import requests

response = requests.get("https://tipsxtra.se/statistics/exportcsv/details/1")

with open('raw_data.csv', 'wb') as file:
    file.write(response.content)


