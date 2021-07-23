from pdfminer.high_level import extract_text
import os
from time import time
from multiprocessing import Pool
import fitz
INICIO = time()
directorio = "../All PDF/"
listado = os.listdir(directorio)
print(listado)
for pdf in listado:
    try:
        archivo = fitz.Document(directorio+pdf)
        paginas = archivo.page_count
        for i in range(0,paginas):
            p = archivo.load_page(i)
            texto = p.get_text()
            if "BDNS" in texto:
                print("Si, esta en la pagina --> ",i+1, " del documento ",pdf)
    except Exception:
        print("**********ERROR**********")
        print("El pdf que da error es --> ",pdf)
        print("*************************")
FINAL = time()

TIEMPO = FINAL - INICIO
print("El tiempo de ejecución es de --> ",TIEMPO)


# Listamos los directorios

"""def lecturaPDF():
    tiempoInicial = time()
    listadoDirectorio = os.listdir("../All PDF")

    for i in listadoDirectorio:
        try:
            text = extract_text("../All PDF/"+i)

            if "BDNS" in text:
                print("El archivo que contiene BDNS es: ",i)
                print("------------------------------------")
        except Exception:
            print("El archivo que da problemas es: ",i)
    tiempoFinal = time()
    tiempoEjecucion = tiempoFinal - tiempoInicial
    print("El tiempo total de ejecución es --> ", tiempoEjecucion)


if __name__ == "__main__":
    pool = Pool()
    pool.map(lecturaPDF(), range(0,5))
    pool.close()"""
