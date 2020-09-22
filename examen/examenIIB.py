# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#  Examen

## 1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros
print("\n1)\n")
arr = np.random.randint(0, 100, 60).reshape(10, 6)

df1 = pd.DataFrame(arr)

# 5 primeros
print(df1.head(5))
# 5 últimos
print(df1.tail(5))


## 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico
print("\n2)\n")
"""
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
"""

arr6x4 = np.random.rand(24).reshape(6, 4)

df2 = pd.DataFrame(arr6x4, columns = ['A', 'B', 'C', 'D'], 
                           index = ['2020-09-15', '2020-09-16',
                                    '2020-09-17', '2020-09-18',
                                    '2020-09-19', '2020-09-20'])

print(df2.loc['2020-09-19', :])


## 4) Crear un Dataframe con 10 registros y 6 columnas y 
# con una propiedad del Dataframe mostrar las columnas, 
# con otro comando mostrar los valores.
print("\n4)\n")
arr4 = np.random.randint(0, 100, 60).reshape(10, 6)
df4 = pd.DataFrame(arr4)
# columnas
df4_columns = df4.columns
print(df4_columns)
# valores
df4_values = df4.values
print(df4_values)



## 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del 
# Dataframe describir estadisticamente el Dataframe
print("\n5)\n")
arr5 = np.random.randint(0, 100, 60).reshape(10, 6)
df5 = pd.DataFrame(arr5)
descripcion_estadistica = df5.describe()
print(descripcion_estadistica)


## 6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos
print("\n6)\n")
arr6 = np.random.randint(0, 100, 60).reshape(10, 6)
df6 = pd.DataFrame(arr6)
df6_transpesta = df6.transpose()

print(df6)
print(df6_transpesta)

## 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 
# 1 vez por cada columna, ascendente y descendente
print("\n7)\n")

arr7 = np.random.randint(0, 100, 60).reshape(10, 6)
df7 = pd.DataFrame(arr7)

df7_sort_col1_asc = df7.sort_values(by=[0], ascending=True)
df7_sort_col1_desc = df7.sort_values(by=[0], ascending=False)
print(df7_sort_col1_asc)
print(df7_sort_col1_desc)

df7_sort_col2_asc = df7.sort_values(by=[1], ascending=True)
df7_sort_col2_desc = df7.sort_values(by=[1], ascending=False)
print(df7_sort_col2_asc)
print(df7_sort_col2_desc)

df7_sort_col3_asc = df7.sort_values(by=[2], ascending=True)
df7_sort_col3_desc = df7.sort_values(by=[2], ascending=False)
print(df7_sort_col3_asc)
print(df7_sort_col3_desc)

df7_sort_col4_asc = df7.sort_values(by=[3], ascending=True)
df7_sort_col4_desc = df7.sort_values(by=[3], ascending=False)
print(df7_sort_col4_asc)
print(df7_sort_col4_desc)

df7_sort_col5_asc = df7.sort_values(by=[4], ascending=True)
df7_sort_col5_desc = df7.sort_values(by=[4], ascending=False)
print(df7_sort_col5_asc)
print(df7_sort_col5_desc)

df7_sort_col6_asc = df7.sort_values(by=[5], ascending=True)
df7_sort_col6_desc = df7.sort_values(by=[5], ascending=False)
print(df7_sort_col6_asc)
print(df7_sort_col6_desc)

df7_sort_full_asc = df7.sort_values(by=[0, 1, 2, 3, 4, 5], ascending=True)
df7_sort_full_desc = df7.sort_values(by=[0, 1, 2, 3, 4, 5], ascending=False)
print(df7_sort_full_asc)
print(df7_sort_full_desc)



## 8) Crear un Dataframe con 10 registros y 6 columnas llenas de números 
# randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7
print("\n8)\n")

arr8 = np.random.randint(0, 10, 60).reshape(10, 6)
df8 = pd.DataFrame(arr8)
df8_condicion = df8 > 7
df8_filtrado = df8[df8_condicion]
print(df8)
print(df8_filtrado)


## 9) Crear un Dataframe con 10 registros y 6 columnas llenas de números 
# randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.
print("\n9)\n")
arr9 = list(np.random.randint(0, 10, 30))
arr9.extend([np.nan for _ in range(30)])
arr9_np = np.array(arr9).reshape(10, 6)
df9 = pd.DataFrame(arr9_np)
df9_fill_na_with_0 = df9.fillna(0)
print(df9)
print(df9_fill_na_with_0)

## 10) Crear un Dataframe con 10 registros y 6 columnas llenas de números 
# randomicos del 1 al 10 y sacar la media, la mediana, el promedio
print("\n10)\n")


arr10 = np.random.randint(0, 10, 60).reshape(10, 6)
df10 = pd.DataFrame(arr10)
df10_media = df10.mean()
df10_mediana = df10.median()
df10_promedio = df10.sum()/10
print(df10)
print(df10_media)
print(df10_mediana)
print(df10_promedio)

## 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números 
# randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 
# 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe
print("\n11)\n")

arr11_1 = np.random.randint(0, 10, 60).reshape(10, 6)
arr11_2 = np.random.randint(0, 10, 60).reshape(10, 6)
df11_1 = pd.DataFrame(arr11_1)
df11_2 = pd.DataFrame(arr11_2)

df11_union = pd.concat([
    df11_1,
    df11_2
    ])

print(df11_1)
print(df11_2)
print(df11_union)



## 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. 
# Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.
print("\n12)\n")

import random

def get_random_string():
    strings = ["hola", "mundo", "como", "estamos", "yo", "nintendo", 
               "aleatorio", "lol", "dataframe", "cadena", "switch",
               "hotel", "transilvania", "random", "pitch", "stereo"]
    index = random.randint(0, len(strings)-1)    
    return strings[index]


arr12 = np.array([get_random_string() for _ in range(60)]).reshape(10, 6)
df12 = pd.DataFrame(arr12)
df12["1y2"] = df12[0] + df12[1]
df12["3y4"] = df12[2] + df12[3]
df12["5y6"] = df12[4] + df12[5]
print(df12["1y2"])
print(df12["3y4"])
print(df12["5y6"])


## 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números 
# randomicos del 1 al 10 enteros, 
# obtener la frecuencia de repeticion de los numeros enteros en cada columna
print("\n13)\n")

arr13 = np.random.randint(0, 10, 60).reshape(10, 6)
df13 = pd.DataFrame(arr13)
df13_frecuencia_col1 = df13[0].value_counts()
df13_frecuencia_col2 = df13[1].value_counts()
df13_frecuencia_col3 = df13[2].value_counts()
df13_frecuencia_col4 = df13[3].value_counts()
df13_frecuencia_col5 = df13[4].value_counts()
df13_frecuencia_col6 = df13[5].value_counts()
print(df13)
print(df13_frecuencia_col1)
print(df13_frecuencia_col2)
print(df13_frecuencia_col3)
print(df13_frecuencia_col4)
print(df13_frecuencia_col5)
print(df13_frecuencia_col6)

## 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, 
# llenas de números randomicos del 1 al 10 enteros. 
# Crear una nueva columna con el calculo por fila (A * B ) / C
print("\n14)\n")

arr14 = np.random.randint(0, 10, 30).reshape(10, 3)
df14 = pd.DataFrame(arr14, columns = ['A', 'B', 'C'])
df14['D'] = (df14['A'] * df14['B'])/ df14['C']
print(df14)
print(df14['D'])



