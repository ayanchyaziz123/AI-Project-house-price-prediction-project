import numpy as np
import pandas as pd

dict = {
    "name":["ayan", "nakib"],
    "age":["20", "20"]
}
df = pd.DataFrame(dict)
print(df)

df1 = pd.read_csv('sylhet.csv')
print(df1.head())
