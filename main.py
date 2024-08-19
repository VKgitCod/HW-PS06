import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.ozon.ru/category/noutbuki-15692/"

driver.get(url)

time.sleep(3)

nouts = driver.find_elements(By.CLASS_NAME, 'j7m_23')

parsed_data = []

for nout in nouts:
    try:
        title = nout.find_element(By.CSS_SELECTOR, 'span.tsBody500Medium').text
        price = nout.find_element(By.CSS_SELECTOR, 'span.tsHeadline500Medium').text
        link = nout.find_element(By.CSS_SELECTOR, 'a.tile-hover-target').get_attribute('href')
    except:
        print("Произошла ошибка при парсинге")
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("nout.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название модели', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)