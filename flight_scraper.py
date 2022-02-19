from selenium.webdriver.common.by import By
from flight import flightObject
import time



class flightScrapingObject:
    def __init__(self, url, driver):
        self.driver = driver
        self.url = url
        self.flights = []
        self.initiate_scraping()

    def print_flights(self):
        for flight in self.flights:
            print(flight)


    def initiate_scraping(self):
        time.sleep(1)

        self.initiate_drive()
        time.sleep(1)

        rows_odd = self.driver.find_elements(By.XPATH, "//tr[@class='flight_row']")

        rows_even = self.driver.find_elements(By.XPATH, "//tr[@class='flight_row css-row_even']")
        rows = rows_even + rows_odd

        print(len(rows))
        for row in rows:
            flight_object = flightObject()
            row_elements = row.find_elements(By.XPATH, ".//*")
            for element in row_elements:
                text_content = element.get_attribute('textContent')
                class_name = element.get_attribute('class')

                if class_name == 'td-airline':
                    flight_object.flight_company = text_content

                if class_name == 'td-flight':
                    flight_object.flight = text_content

                if class_name == 'td-city':
                    flight_object.landing_from = text_content

                if class_name == 'td-terminal':
                    flight_object.terminal = text_content

                if class_name == 'td-scheduledTime':
                    flight_object.scheduled_time = text_content

                if class_name == 'td-updatedTime':
                    flight_object.updated_time = text_content

                if class_name == 'dt-cell d-none d-lg-table-cell row-status':
                    flight_object.status = text_content

            self.flights.append(flight_object)
        print(self.flights)

    def close_driver(self):
        self.driver.close()

    def initiate_drive(self):
        time.sleep(1)
        time.sleep(1)

        self.driver.get(self.url)
        time.sleep(1)
        time.sleep(1)
