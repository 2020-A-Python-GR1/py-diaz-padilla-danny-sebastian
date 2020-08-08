# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:01:18 2020

@author: COMPANY
"""
import xlsxwriter
import pandas as pd


path_guardado = "../03-pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519, :].copy()

num_artistas = sub_df['artist'].value_counts()
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)



workbook = xlsxwriter.Workbook('chart_bar.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Nombre', 'Cantidad']
data = [
    num_artistas.index,
    num_artistas.values,
]


worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])


chart1 = workbook.add_chart({'type': 'bar'})

# Configure the first series.
chart1.add_series({
    'categories': '=Sheet1!$A$2:$A${}'.format(len(num_artistas.index) + 1),
    'values':     '=Sheet1!$B$2:$B${}'.format(len(num_artistas.index) + 1),
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Conteo de artistas'})
chart1.set_x_axis({'name': 'Conteo'})
chart1.set_y_axis({'name': 'Nombre de artista'})

# Set an Excel chart style.
chart1.set_style(11)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

workbook.close()
