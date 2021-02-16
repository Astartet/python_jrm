from bs4 import BeautifulSoup
archivo = input("Nombre del archivo HTML: ")
directorio_html = ".\html_files\\"
directorio_csv = ".\csv_files\\"
with open(directorio_html+archivo, 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents,'html.parser')
    table = soup.find('table', {'class' : 'display compact no-footer dataTable'})
    formateado = open(directorio_html+'tabla_'+archivo,'a')
    print(table,file=formateado)


import os
import pandas as pd 

htmlname = archivo
html = open(directorio_html+'tabla_'+htmlname,'r')
source_code = html.read()
tables = pd.read_html(source_code)

for i,table in enumerate(tables):
    table.to_csv(directorio_csv+archivo+'.csv'.format(i),'*')
