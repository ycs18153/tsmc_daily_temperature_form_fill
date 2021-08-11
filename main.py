from selenium import webdriver
import random
import time
import os
import threading


def auto_fill(employee_id, vaccinated):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument(
            "user-agent = Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")
        options.add_argument('blink-settings=imagesEnabled=false')
        options.add_argument("--disable-javascript")
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        driver = webdriver.Chrome(executable_path=os.environ.get(
            "CHROMEDRIVER_PATH"), chrome_options=options)
        # driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        temperature = round(random.uniform(36.1, 37.3), 1)
        driver.implicitly_wait(20)
        driver.get('https://zh.surveymonkey.com/r/EmployeeHealthCheck')
        print(f'{employee_id}\'s task begin')
        driver.find_element_by_id('683674386_4495696088').click()
        driver.find_element_by_id('683674383').send_keys(employee_id)
        driver.find_element_by_id('683674388_4495696090').click()
        driver.find_element_by_id('683674384').send_keys(str(temperature))
        driver.find_element_by_id('683674400_4495696174').click()
        driver.find_element_by_id('683674393_4495696115').click()
        if vaccinated:
            driver.find_element_by_id('683711504_4495952678').click()
        else:
            driver.find_element_by_id('683711504_4495952679').click()
        driver.find_element_by_id('683674394_4495717677').click()
        driver.find_element_by_id('683674398_4495718982').click()
        driver.find_element_by_id('683674395_4495696119').click()
        driver.find_element_by_id('683674397_4495696166').click()
        driver.find_element_by_id('683674385_4495696080').click()
        driver.find_element_by_xpath(
            "//button[@class='btn small next-button survey-page-button user-generated notranslate']").click()
        print(f'{employee_id}\'s task done')
    except:
        print(f'{employee_id}\'s task failed')


if __name__ == "__main__":
    start_time = time.time()
    # 元倉: 120513, 培權: 120557, 有璿: 120535, 錢玟: 120487, 書文: 120649, 可芸: 120650, 郁婷: 120524, 相程: 113531, 郭同益: 120651
    employee_with_vaccine = ['120451', '120487']
    employee_without_vaccine = [
        '120513', '120557', '120535', '120649', '120650', '120524', '113531', '120651']
    threads = []
    for i in range(len(employee_with_vaccine)):
        threads.append(threading.Thread(target=auto_fill,
                       args=(employee_with_vaccine[i], True)))
    for j in range(len(employee_without_vaccine)):
        threads.append(threading.Thread(target=auto_fill,
                       args=(employee_without_vaccine[j], False)))
    for k in range(len(threads)):
        threads[k].start()
    for l in range(len(threads)):
        threads[l].join()
    end_time = time.time()
    print(f'takes {end_time - start_time} s')
