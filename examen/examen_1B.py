# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


# 1) Examen

## 2) Crear un vector de ceros de tamaño 10
vector_ceros = np.zeros(10)
print("Crear un vector de ceros de tamaño 10\n", vector_ceros, "\n")

## 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1
vector_ceros_2 = np.zeros(10)
vector_ceros_2[4] = 1
print("Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1\n", vector_ceros_2, "\n")

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.
vector_50 = np.arange(1, 50, 1)
print("Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc\n", vector_50, "\n")
vector_50_inverso = vector_50[::-1]
print("Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc\n", vector_50_inverso, "\n")

## 5) Crear una matriz de 3 x 3 con valores del cero al 8
matriz_3_3 = np.arange(0, 9, 1).reshape(3, 3)
print(" Crear una matriz de 3 x 3 con valores del cero al 8\n", matriz_3_3, "\n")


## 6) Encontrar los indices que no sean cero en un arreglo

arreglo = [1,2,0,0,4,0]
indices_arreglo = []
for indice, numero in enumerate(arreglo):
    if numero != 0:
        indices_arreglo.append(indice)
        
print(" Encontrar los indices que no sean cero en un arreglo\narreglo: ", arreglo, "\nIndices que no son cero: ", indices_arreglo, "\n")


## 7) Crear una matriz de identidad 3 x 3 

matriz_identidad = np.ones((3, 3))
print("Crear una matriz de identidad 3 x 3 \n", matriz_identidad, "\n")

## 8) Crear una matriz 3 x 3 x 3 con valores randomicos
matriz_3_3_3_random = np.random.rand(3, 3)
print("Crear una matriz 3 x 3 x 3 con valores randomicos\n", matriz_3_3_3_random, "\n")


## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor
matriz_10_10 = np.arange(1, 101, 1).reshape((10, 10))
print("Crear una matriz 10 x 10 y encontrar el mayor y el menor\nMatriz: ", matriz_10_10, "\nMenor: ", np.min(matriz_10_10), "\nMayor", np.max(matriz_10_10),"\n")


## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)


from scipy import misc
imagen = misc.face()[1:20, 1:20, :]  # para facilitar el procesamiento solo se toma los primeros 20x20 pixeles RGB
colores_unicos = []
alto = imagen.shape[0]
ancho = imagen.shape[1]

print("Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)\nPara la imagen las siguientes dimensiones se calculará: ", imagen.shape)


for row in range(alto):
    for col in range(ancho):
        
        color = np.array(imagen[row][col])
        
        color_existente = False        
        for color_unico in colores_unicos:        
            if color[0] == color_unico[0] and color[1] == color_unico[1] and color[2] == color_unico[2]:
                color_existente = True
                break
                
        if not color_existente:
            colores_unicos.append(color)

print("Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)\nPara la imagen con dimensiones: ", imagen.shape, "\nHay ", len(colores_unicos) , " colores RGB únicos\n")



## 11) ¿Como crear una serie de una lista, diccionario o arreglo?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

series_lista = pd.Series(mylist)
print(" ¿Como crear una serie de una lista, diccionario o arreglo? Lista: \n", series_lista, "\n")
series_arr = pd.Series(myarr)
print(" ¿Como crear una serie de una lista, diccionario o arreglo? Arreglo: \n", series_arr, "\n")
series_dict = pd.Series(mydict)
print(" ¿Como crear una serie de una lista, diccionario o arreglo? Dict: \n", series_dict, "\n")


## 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?



ser = pd.Series(mydict)

# Transformar la serie en dataframe y hacer una columna indice

df0 = pd.DataFrame(ser)
df0 = df0.assign(indices_copiados=df0.index)







## 13) ¿Como combinar varias series para hacer un DataFrame?


ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df1 = pd.DataFrame()
df1[0] = ser1
df1[1] = ser2

print(" ¿Como combinar varias series para hacer un DataFrame? df1[0] = ser1, df1[1] = ser2\n", df1, "\n")




## 14) ¿Como obtener los items que esten en una serie A y no en una serie B?


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


mask = ~ser1.isin(ser2)
datos_a_no_en_b = ser1[mask]




## 15) ¿Como obtener los items que no son comunes en una serie A y serie B?


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

mask1 = ~ser1.isin(ser2)
mask2 = ~ser2.isin(ser1)

items_no_comunes = pd.concat([
    ser1[mask1],
    ser2[mask2],
    ])




##############
## 16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))




## 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?


np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

####################



## 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?

# Se hace reshape a los valores de la serie

# shape(7,5)
ser = pd.Series(np.random.randint(1, 10, 35)).values.reshape((7, 5))
df_shape_definido = pd.DataFrame(ser)
print(df_shape_definido)




## 19) ¿Obtener los valores de una serie conociendo la posicion por indice?



ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u

valor_serie_por_posicion = ser[pos]
print(valor_serie_por_posicion)







## 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?



ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

# nueva columna
df3 = pd.DataFrame(ser1)
df3[1] = ser2





## 21)¿Obtener la media de una serie agrupada por otra serie?

# `groupby` tambien esta disponible en series.



frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64




## 22)¿Como importar solo columnas especificas de un archivo csv?

# https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.











