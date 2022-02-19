import os
from flight_scraper import flightScrapingObject
from selenium import webdriver

os.environ['PATH'] += r"C:/chromedriver"

url = 'https://www.iaa.gov.il/airports/ben-gurion/flight-board'
driver = webdriver.Chrome()
driver.maximize_window()

folder_name = 'flights'

fso = flightScrapingObject(url=url, driver=driver, folder_name=folder_name)
fso.load_objects()

fso.initiate_scraping()

fso.save_object()

fso.print_flights()

fso.update()
