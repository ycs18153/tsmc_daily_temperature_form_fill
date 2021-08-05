from selenium import webdriver
import random
from datetime import datetime
import schedule
import time


def daily_temperature_form_fill():
    driver = webdriver.Chrome('./chromedriver')
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


schedule.every().day.at('07:30').do(daily_temperature_form_fill)
if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(10)
