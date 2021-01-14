import mechanize
from selenium.webdriver import Chrome
url = "http://localhost/form_test/from_test.html"
driver = Chrome(executable_path='C:\Program Files (x86)\chromedriver\chromedriver.exe')
driver.get(url)
br = mechanize.Browser()
br.open("http://localhost/form_test/from_test.html")
br.select_form(nr=0)
br.form['nombre'] = 'jorge'
req = br.submit()