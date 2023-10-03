import pandas as pd

#insertar datos
d={"Articulo":["Coca Cola", "Tostitos", "Cheetos", "Jugo"],
   "Precio":[17,35,20,22],
   "Costo":[8,17,10,11], "Categoría":["Bebida","Botana","Botana", "Bebida"]}

data= pd.DataFrame(d) #Dataframe vacio ()
#Read leer archivo
print(data)

"""""
#Listas de lista
art= [
    ["Tostitos",35,17,"Botana"],
    ["Coca Cola",17,8,"Bebida"],
    ["Cheetos",20,10, "Botana"],
    ["Jugo",22,11,"Bebida"]
]

data2=pd.DataFrame(art, columns= ["Articulo","Precio","Costo","Categoría"])
print(data2)
"""

print(data.Articulo)
print(data["Articulo"])

columnas=["Articulo","Precio"]
print(columnas)

#Calcular las utilidade de cada producto (precio-costo)
#print("Resta")
#print(data.Precio - data.Costo)
Utilidad =data.Precio - data.Costo
data["Utilidad"]= Utilidad
print(data)

#Calcular que articulo(s) tienen el precio mayor
maximo= max(data.Precio)
print("Max")
#print(data[data.Precio==maximo])
#Otra forma
filtro = data.Precio==maximo
print(filtro)
print(data[filtro][columnas])

#Calcular que articulo(s) tienen el precio mayor de la categoria bebidas
data_filtrado=data[data.Categoría=="Bebida"]
print("\n")
print(data_filtrado)
maximo2=data_filtrado.Precio.max()
filtro2 = data_filtrado.Precio == maximo2
print(data_filtrado[filtro2][columnas])

#Calcular max, min, mean de las columans precio, costo, y devolberlo en un dataframe

print("\nmaximos")
columnas =["Precio","Costo"]
maximos = data[columnas].max()
minimos = data[columnas].min()
promedios = data[columnas].mean()
print(type(maximos))
print(maximos)

res = pd.DataFrame([maximos,minimos,promedios], index= ["max","min","promedio"])
print(res)