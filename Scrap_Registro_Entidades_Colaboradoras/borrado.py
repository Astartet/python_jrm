import os

directorio_html = ".\html_files\\"
directorio_csv = ".\csv_files\\"

borrar = "rmdir /Q /S "+directorio_csv
borrar2 = "rmdir /Q /S "+directorio_html

# Borramos la carpeta
os.system(borrar)
os.system(borrar2)

# Creamos la carpeta
carpeta = "mkdir "+directorio_html
carpeta2 = "mkdir "+directorio_csv
os.system(carpeta)
os.system(carpeta2)