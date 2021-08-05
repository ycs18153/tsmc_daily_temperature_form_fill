from selenium import webdriver
import random
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument(
    "user-agent = Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")
options.add_argument('blink-settings=imagesEnabled=false')
options.add_argument("--disable-javascript")
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(
    'executable_path=os.environ.get("CHROMEDRIVER_PATH")', chrome_options=options)
employee_id = '120451'
temperature = round(random.uniform(36.1, 37.3), 1)

driver.get('https://zh.surveymonkey.com/r/EmployeeHealthCheck')

driver.find_element_by_id('683674386_4495696088').click()
driver.find_element_by_id('683674383').send_keys(employee_id)
driver.find_element_by_id('683674388_4495696090').click()
driver.find_element_by_id('683674384').send_keys(str(temperature))
driver.find_element_by_id('683674400_4495696174').click()
driver.find_element_by_id('683674393_4495696115').click()
driver.find_element_by_id('683711504_4495952678').click()
driver.find_element_by_id('683674394_4495717677').click()
driver.find_element_by_id('683674398_4495718982').click()
driver.find_element_by_id('683674395_4495696119').click()
driver.find_element_by_id('683674397_4495696166').click()
driver.find_element_by_id('683674385_4495696080').click()
driver.find_element_by_xpath(
    "//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()

driver.close()
