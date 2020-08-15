# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:26 2020

@author: COMPANY
"""


import pandas as pd
import numpy as np

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

# loc, filtro por labels

filtrado_horizontal = df.loc[1035]
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index)

serie_vertical = df['artist']

print(serie_vertical)
print(serie_vertical.index)



df_1035 = df[df.index == 1035]


segundo = df.loc[1035]
segundo = df.loc[[1035, 1036]]
segundo = df.loc[3:5]
segundo = df.loc[1035, 'artist']
segundo = df.loc[1035, ['artist', 'medium']]


# iloc, filtro con n+umeros
tercero = df.iloc[0]
tercero = df.iloc[[0, 1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:4]



#######################




datos = {
    "nota 1":{
        "Pepito": 7,
        "Juanita": 9,
        "Maria": 9
        },
    "nota 2":{
        "Pepito": 7,
        "Juanita": 9,
        "Maria": 9
        },
    "disciplina":{
        "Pepito": 4,
        "Juanita": 9,
        "Maria": 2
        
        }
    }
    


notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] <= 7
condicion_nota2 = notas["nota 2"] <= 7
condicion_disc = notas["disciplina"] <= 7

mayores_siete = notas.loc[condicion_nota, ["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota2][condicion_disc]





notas.loc["Maria", "disciplina"] = 7
notas.loc[:, "disciplina"] = 7


####### Promedio de las 3 notas


notas["promedio"] = notas.mean(axis=1)

















# END