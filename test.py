import os
from flight_scraper import flightScrapingObject
from selenium import webdriver

os.environ['PATH'] += r"C:/chromedriver"

url = 'https://www.iaa.gov.il/airports/ben-gurion/flight-board'
driver = webdriver.Chrome()

fso = flightScrapingObject(url=url, driver=driver)

fso.print_flights()