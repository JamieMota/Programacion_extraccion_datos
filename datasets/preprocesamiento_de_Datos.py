import pandas as pd
datos= pd.read_csv("surveys.csv")
#print(datos.sample(10))

nulos = datos.isnull()
#print(nulos.any())
#print(nulos.sum())
#print(nulos.sum().sum())
#print(nulos.sum()/len(nulos))

#Eliminar columnas
datos_eliminados= datos.drop(["day","month"],axis="columns") #drop trabaja con copias en numpy
#print(datos.columns)
#print(datos_eliminados.columns)

#Eliminar columnas original
datos.drop(["day","month"],axis="columns", inplace=True) #inplace es para trabajar con el original
print(datos.columns)

#Eliminar renglones
datos_row_eliminados=datos.drop([2,3,4], axis="index")
#print(datos_row_eliminados.head(10))

#Eliminar nulos
datos_no_nulos=datos.dropna(axis="index",thresh=4)
print(len(datos))
print(len(datos_no_nulos))

#Llenar datos nulos
#promedios=datos.mean()  #Esta mal
#print(promedios)
#datos_llenos=datos.fillna("Sin datos")
#print(datos_llenos)

#Llenar valores
datos_ffill = datos.ffill()
print(datos_ffill)

datos_mix=datos.bfill().ffill()
print(datos_mix)

#Verificar duplicados
duplicados=datos.duplicated()
duplicados=datos.duplicated(subset=["sex","weight"])
print(duplicados.head(15))

eliminar_duplicados=datos.drop_duplicates(subset=["sex","weight"])
print(eliminar_duplicados)