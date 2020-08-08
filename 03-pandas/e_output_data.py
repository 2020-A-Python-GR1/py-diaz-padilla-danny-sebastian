# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:31:16 2020

@author: COMPANY
"""

import pandas as pd
import sqlite3

import xlsxwriter

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519, :].copy()

# Tipos Archivos: Json, Excel, SQL


path_excel = "./data/artwork_data.xlsx"
path_excel_indice = "./data/artwork_data_indice.xlsx"
path_excel_columnas = "./data/artwork_data_columns.xlsx"
 
sub_df.to_excel(path_excel)
sub_df.to_excel(path_excel_indice, index=False)


columnas = ['artist', 'title', 'year']
sub_df.to_excel(path_excel_columnas, columns=columnas)



path_excel_mt = "./data/artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt, engine='xlsxwriter')
sub_df.to_excel(writer, sheet_name='Primera')
sub_df.to_excel(writer, sheet_name='Segunda')
sub_df.to_excel(writer, sheet_name='Tercera')
writer.save()


# Formato condicional 
path_excel_colores = "./data/artwork_data_colores.xlsx"

num_artistas = sub_df['artist'].value_counts()

writer = pd.ExcelWriter(path_excel_colores, engine='xlsxwriter')

num_artistas.to_excel(writer, sheet_name='artistas')
hoja_artistas = writer.sheets['artistas']
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

formato_artistas = {
    "type": "2_color_scale",
    "min_value": "10",
    "min_type": "percentile",
    "max_value": "99",
    "max_type": "percentile"
    
    }

hoja_artistas.conditional_format(rango_celdas, formato_artistas)





writer.save()




"""

with sqlite3.connect('bdd_artist.bdd') as conexion:
    sub_df.to_sql('py_artistas', conexion)
    
    

sub_df.to_json('artistas.json')
sub_df.to_json('artistas_tabla.json', orient='table')







chart1 = workbook.add_chart({'type': 'bar'})

# Configure the first series.
chart1.add_series({
    'name':       '=artistas!$B$1',
    'categories': '=artistas!$A$2:$A$7',
    'values':     '=artistas!$B$2:$B$7',
})

# Configure a second series. Note use of alternative syntax to define ranges.
chart1.add_series({
    'name':       ['artistas', 0, 2],
    'categories': ['artistas', 1, 0, 6, 0],
    'values':     ['artistas', 1, 2, 6, 2],
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Conteo de artistas'})
chart1.set_x_axis({'name': 'Test number'})
chart1.set_y_axis({'name': 'Sample length (mm)'})

# Set an Excel chart style.
chart1.set_style(11)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

"""







# FIN

























