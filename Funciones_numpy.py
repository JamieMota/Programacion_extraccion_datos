#Mota Parra Jamie Valeria
import numpy as np
l=[[1,2,3,4,5], [6,7,8,9,10]]
n1 = np.array(l)
print(l)
print(type(n1))

#principales atributos

print(n1.ndim)
print(n1.shape)
print(n1.size)
print(n1.dtype)

#Acceso a elementos
print(n1[1,2]) # primer numero es el renglon y el segundo es la columna
print(n1 * 2)

print(np.linalg.norm(n1))
print(n1.T)
print(n1.transpose())
print(n1.mean())
print(n1[0,:].mean())

"""
   Ecuaciones
    x + 2y = 1
    3x + 5y = 2
"""
ecuaciones = [[1,2],[3,5]]
resultados = np.array([1,2])
np_ecuaciones = np.array(ecuaciones)
resultados= np.array([1,2])
print(np.linalg.solve(np_ecuaciones,resultados))