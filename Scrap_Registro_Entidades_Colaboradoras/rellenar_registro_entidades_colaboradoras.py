from selenium import webdriver
import requests
from time import sleep

# URL Objetivo

webpage = r"https://incentivos.agenciaandaluzadelaenergia.es/Orden2016SIG/listado.jsp"
directorio_html = ".\html_files\\"

# Parámetros formulario

linea = "PYME SOSTENIBLE"
provincia = "CÓRDOBA"
registros = 100
# Apertura del navegador
driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')


driver.get(webpage)
sleep(5)
# Introduccion del parametro LINEA en el formulario
sbox = driver.find_element_by_id('LINEA')
sbox.send_keys(linea)
sleep(5)
# Introduccion del parametro PROVINCIA en el formulario
ciudad = driver.find_element_by_name('PROV')
ciudad.send_keys(provincia)
sleep(5)

# Pulsacion del botón FILTRAR
submit = driver.find_element_by_id('filt')
submit.click()

sleep(5)
# Numeros de registros mostrados
lista = driver.find_element_by_name('lAtAbla_length')
lista.send_keys(registros)
sleep(5)

# Guardamos el código html

f = open(directorio_html+'registro1.html', 'a')
print(driver.page_source, file=f)
f.close()

# pagina siguiente
siguiente = driver.find_element_by_id('lAtAbla_next')
siguiente.click()
sleep(2)
# Guardamos el código html

f2 = open(directorio_html+'registro2.html', 'a')
print(driver.page_source, file=f2)
f2.close()


# pagina siguiente
siguiente = driver.find_element_by_id('lAtAbla_next')
siguiente.click()
sleep(2)
# Guardamos el código html

f3 = open(directorio_html+'registro3.html', 'a')
print(driver.page_source, file=f3)
f3.close()


# pagina siguiente
siguiente = driver.find_element_by_id('lAtAbla_next')
siguiente.click()
sleep(2)
# Guardamos el código html

f4 = open(directorio_html+'registro4.html', 'a')
print(driver.page_source, file=f4)
f4.close()


# pagina siguiente
siguiente = driver.find_element_by_id('lAtAbla_next')
siguiente.click()
sleep(2)
# Guardamos el código html

f5 = open(directorio_html+'registro5.html', 'a')
print(driver.page_source, file=f5)
f5.close()


