from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data
from data import *
from tkinter import *
import os
import time

def entry():
    ua = 'Mozilla/5.0 (Linux; Android 9; SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={ua}")
    #options.add_argument('--proxy-server=%s' % '212.81.36.197:9091')
    #options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    surname = data.surname
    name = data.name
    patr = data.patr
    pass_num = data.pass_num
    region = data.region

    try:
        wait = WebDriverWait(driver, 500)
        driver.get('https://checkege.rustest.ru/')
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"captcha-img\"]")))

        surname_field = driver.find_element(By.XPATH, '//*[@id="surname"]').send_keys(surname)
        name_field = driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(name)
        patr_field = driver.find_element(By.XPATH, '//*[@id="patr"]').send_keys(patr)
        pass_num_field = driver.find_element(By.XPATH, '//*[@id="passNum"]').send_keys(pass_num)
        captha_field = driver.find_element(By.XPATH, '//*[@id="captcha"]')
        driver.execute_script("document.getElementById('region').style.display = 'block';")
        Select(driver.find_element(By.XPATH, '//*[@id="region"]')).select_by_value(region)

        driver.execute_script("scroll(0, 250);")
        captha = driver.find_element(By.XPATH, '//*[@id="captcha-img"]')
        captha.screenshot("captha.png") # captha_get
        result_captcha = captha_user_solver()
        captha_field.send_keys(result_captcha)

        driver.find_element(By.XPATH, '//*[@id="submit-btn"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"table-container\"]")))

        driver.save_screenshot("result.png")

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def captha_user_solver():
    #os.system("captha.png")
    solve_captha = input('Введите капчу: ')
    return solve_captha



def main():
    entry()





if __name__ == "__main__":
    main()