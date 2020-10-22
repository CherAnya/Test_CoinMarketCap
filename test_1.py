import selenium
import time
import requests
import pandas as pd
import numpy as np
import threading
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.keys import Keys

# создание датафрейма для записи данных
columns = ['Name', 'Price', '24h', '7d', 'Market_Cup', 'Volume', 'Circulating_Supply']
df = pd.DataFrame(columns = columns)

# функция к заданию 1_1
def test_1():
    try:
        link = "https://coinmarketcap.com/"
        
        browser = webdriver.Chrome()
        
        # время отклика веб-сайта         
        time = requests.get(link).elapsed.total_seconds()
        
        # открытие браузера на весь экран         
        browser.maximize_window()
        
        browser.get(link)
        
        # скроллим вниз
        browser.execute_script('window.scrollBy(0, 500);')
        
        # сортировка по убыванию объема         
        button = browser.find_element_by_xpath("//p[contains(text(), 'Volume')]")
        button.click()
        
        for i in range(10):
            # поиск элемента на странице             
            Name_element = browser.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[3]/a/div/div/p")
            # получение данных             
            Name = Name_element.text
            # запись в датафрейм            
            df.loc[i, 'Name'] = Name
            Price_element = browser.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[4]/div/a")
            Price = Price_element.text
            df.loc[i, 'Price'] = Price
            h24_element = browser.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[5]/div/div/p")
            h24 = h24_element.text
            df.loc[i, '24h'] = h24
            d7_element = browser.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[6]/div/div/p")
            d7 = d7_element.text
            df.loc[i, '7d'] = d7
            Market_Cup_element = browser.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[7]/p")
            Market_Cup = Market_Cup_element.text
            df.loc[i, 'Market_Cup'] = Market_Cup
            Volume_element = browser.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[8]/div/a/p")
            Volume = Volume_element.text
            df.loc[i, 'Volume'] = Volume
            Circulating_Supply_element = browser.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[" + str(i + 1) + "]/td[9]/div/div/p")
            Circulating_Supply = Circulating_Supply_element.text
            df.loc[i, 'Circulating_Supply'] = Circulating_Supply
        
    finally: 
        browser.quit()
        
    # сохранение данных в файл
    df.to_csv(r'C:\Решение_тестового_задания_Чересова\output.csv', sep=';', index = None)
        
    # вывод времени отклика веб-сайта     
    print('Время отклика веб-сайта, с:', time)

test_1()