from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
palabras = ["huawei ATN","ATN 950D","ATN 980C","ATN 910C-G","ATN 910D-A", "HuaweiATN","Router & Huawei", "Huawei Router", "V300R006C10", "V300R006C10SPC300","VRP Huawei", "Huawei Versatile Routing Platform", "ATN Series", "TCP", "TLS", "SSH", "NTP", "Syslog", "Huawei exploit"]
#url = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=+""+&search_type=all&isCpeNameSearch=false"
driver = webdriver.Chrome(executable_path="/home/jorge/chromedriver", options=options)
"""for i in palabras:
    url = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query="+i+"&search_type=all&isCpeNameSearch=false"
    driver.get(url)
    sleep(3)
driver.close()

for i in palabras:
    url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="+i
    driver.get(url)
    sleep(3)

driver.close()

for i in palabras:
    url = "https://www.tenable.com/plugins/search?q="+i+"&sort=&page=1"
    driver.get(url)
    sleep(3)
driver.close()
id = "gdprClose"
for i in palabras:
    url = "https://www.rapid7.com/db/?q="+i+"&type=nexpose"
    driver.get(url)
    sleep(3)
driver.close()

for i in palabras:
    url = "https://www.huawei.com/en/searchresult?keywords="+i+"&contenttype=Security-Bulletins"
    driver.get(url)
    driver.save_screenshot(i+".png")
    sleep(3)
driver.close()

for i in palabras:
    url = "https://github.com/search?q="+i
    driver.get(url)
    sleep(3)
driver.close()"""



url = "https://www.kb.cert.org/vuls/search/"
driver.get(url)
sleep(1)
search = driver.find_element_by_id("id_wordSearch").send_keys("huawei ATN")
sleep(1)
search.send_keys(Keys.ENTER)


