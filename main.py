from selenium import webdriver
import random
import os
import multiprocessing as mp


def auto_fill(employee_id, vaccinated):
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
    driver.get('https://zh.surveymonkey.com/r/EmployeeHealthCheck')
    print("browser opening")
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
    print("task done")


if __name__ == "__main__":
    processes = []
    p1 = mp.Process(target=auto_fill, args=('120451', True, ))
    processes.append(p1)
    p2 = mp.Process(target=auto_fill, args=('120513', False, ))
    processes.append(p2)
    p3 = mp.Process(target=auto_fill, args=('120557', False, ))
    processes.append(p3)
    p4 = mp.Process(target=auto_fill, args=('120535', False, ))
    processes.append(p4)
    p5 = mp.Process(target=auto_fill, args=('120487', False, ))
    processes.append(p5)
    p6 = mp.Process(target=auto_fill, args=('120649', False, ))
    processes.append(p6)

    for p in processes:
        p.start()
    for p in processes:
        p.join()
    # 元倉: 120513, 培權: 120557, 有璿: 120535, 錢玟: 120487, 書文: 120649
    # employee_with_vaccine = ['120451']
    # employee_without_vaccine = ['120513', '120557', '120535', '120487', '120649']
    # pool = mp.Pool(os.cpu_count())
    # res = pool.map(vaccine, employee_with_vaccine)
    # print(res)
