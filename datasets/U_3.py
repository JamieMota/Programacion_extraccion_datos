import pandas as pd

data = pd.read_csv("datasets/data_olimpiadas.csv",
                   index_col = 0)

print(data.sample(5))