import pandas as pd
import numpy as np

df = pd.read_csv("D:/TryCatch/data/features.csv")
print(df.head(5))
df.drop_duplicates()

# print(df.info)