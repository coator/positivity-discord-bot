import numpy as np
import pandas as pd



newset = pd.read_csv('raccoon-society-phrases.csv')

for item in newset:
    print(item)