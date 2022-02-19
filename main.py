import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


os.environ['PATH'] += r"C:/chromedriver"

driver = webdriver.Chrome()
url = 'https://www.iaa.gov.il/airports/ben-gurion/flight-board'
time.sleep(2)

driver.get(url)
time.sleep(2)
#
# button = driver.find_elements(By.XPATH, "//button[@class='btn btn-primary rounded-pill js-load-more-flight-results']")
# while len(button) > 0:
#     print('click')
#     button.click()
#     button = driver.find_elements(By.XPATH, "//button[@class='btn btn-primary rounded-pill js-load-more-flight-results']")

# articles = driver.find_elements(By.XPATH, "//tr[@class='flight_row css-row_even']")
# print(articles)
# # flight_row css-row_even
# #print(i.find_elements_by_xpath(".//*"))
#
# print(len(articles))
# for i in articles:
#     print('new object')
#
#     for j in i.find_elements_by_xpath(".//*"):
#         if j.get_attribute('class') == 'td-airline':
#             print('Flight company:', j.get_attribute('textContent'))
#         if j.get_attribute('class') == 'td-flight':
#             print('Flight:', j.get_attribute('textContent'))
#         if j.get_attribute('class') == 'td-city':
#             print('landing from:', j.get_attribute('textContent'))
#         if j.get_attribute('class') == 'td-terminal':
#             print('Terminal:', j.get_attribute('textContent'))
#         if j.get_attribute('class') == 'td-scheduledTime':
#             print('scheduled Time:', j.get_attribute('textContent'))
#         if j.get_attribute('class') == 'td-updatedTime':
#             print('Updated Time:', j.get_attribute('textContent'))
#         if j.get_attribute('class') == 'dt-cell d-none d-lg-table-cell row-status':
#             print('Status:', j.get_attribute('textContent'))


driver.close()