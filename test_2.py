import selenium
import time
import requests
import pandas as pd
import numpy as np

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.keys import Keys

# функция к заданию 2
def test_2():
    try:
        link = "https://coinmarketcap.com/"
        
        browser = webdriver.Chrome()
        
        # открытие браузера на весь экран         
        browser.maximize_window()
        
        browser.get(link)
        
        print('Выберите язык из списка ниже (например, RU):')
        
        # нажатие на кнопку выбора языка         
        button = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/div/button')
        button.click()
        
        # вывод всех возможных языков пользователю           
        for i in range(27):
            lang_element_1 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[2]/div[' + str(i + 1) + ']/a')
            lang_name_1 = lang_element_1.text
            print(lang_name_1)
            
        # ввод языка пользователем         
        lang = input('Язык: ')
        
        for j in range(27):
            lang_element_2 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[2]/div[' + str(j + 1) + ']/a/span[2]')
            lang_name_2 = lang_element_2.text
            if lang_name_2 == lang:
                input_1 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/div[2]/form/div/input')
                input_1.send_keys(lang)
                button_1 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[1]')
                button_1.click()
                break
        
        # для проверки правильности выбранного языка         
        time.sleep(30)
        
    finally: 
        browser.quit()

test_2()