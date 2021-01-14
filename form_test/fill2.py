from selenium import webdriver

webpage = r"http://localhost/form_test/from_test.html"

searchterm ="prueba"
select_ciudad = "Sevilla"

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver\chromedriver.exe')
driver.get(webpage)

sbox = driver.find_element_by_name('nombre')
sbox.send_keys(searchterm)
ciudad = driver.find_element_by_name('ciudad')
ciudad.send_keys(select_ciudad)
submit = driver.find_element_by_name("enviar")
submit.click()