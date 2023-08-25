import pandas as pd

datos = {
    "Nombres":["Franco","Maria","Jamie"],
    "Materias":["Matematicas","Programacion","Mercadotecnia"],
    "Promedios":[80,90,100]
}

df_alumnos = pd.DataFrame(datos)
print(df_alumnos)

df_colesterol= pd.read_csv("https://raw.githubusercontent.com/asalber"
            "/manual-python/master/datos/colesteroles.csv", sep=";"
                           , decimal=",")
print(df_colesterol)

print(df_colesterol.head(3))

print(df_colesterol.shape)
print(df_colesterol.size)
print(df_colesterol.columns)
print(df_colesterol.dtypes)
print(df_colesterol.index)
print(df_colesterol.nombre)

df_colesterol["colesterol"].plot()