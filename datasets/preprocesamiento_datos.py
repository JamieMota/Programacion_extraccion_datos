import pandas as pd

datos= pd.read_csv("datasets/surveys.csv")
print(datos.sample(10))

nulos = datos.isnull()
print(nulos.any)