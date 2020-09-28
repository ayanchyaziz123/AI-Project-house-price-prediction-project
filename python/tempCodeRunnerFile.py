import pandas as pd
import numpy as np


dict1 = {
    "name":["rohan", "ayan", "nakib"],
    "city":["sylhet", "dhaka", "rongpur"],
    "marks":["10", "20", "30"]
}
df = pd.DataFrame(dict1)
print(df)