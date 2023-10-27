import pandas as pd

alumnos = {
    "nombre": ["Juan","Maria","Pedro","Miguel"],
    "edad": [20,19,22,18],
    "carrera":["IN","C","NI","IN"],
    "promedio":[90,85,70,100]
}
df_alumnos = pd.DataFrame(alumnos)

#Busquedas <>
#and - &
#or |
#neg ~
# Tecnica 1. Filtrado de datos
c1=df_alumnos.promedio>80
data_c1= df_alumnos[c1]
print(data_c1)
print("\n")
c2= df_alumnos.promedio>80 & (df_alumnos.carrera== "IN")
data_c2= df_alumnos[c2]
print(data_c2)

print("\n")

#Tecnica2. Busqueda por query
query1_c1= df_alumnos.query("promedio > 80")
print(query1_c1)


query2_c2 = df_alumnos.query("promedio>80 and carrera =='IN'")
print(query2_c2)
#Otra forma
condicion="promedio>80 and carrera =='IN'"
query2_c2 = df_alumnos.query(condicion)