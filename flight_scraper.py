import os

import keyboard
from selenium.webdriver.common.by import By

from file_manager import save_list_of_obj, load_list_of_json
from flight import flightObject
import time
from tqdm import tqdm


class flightScrapingObject:
    def __init__(self, url, driver, folder_name):
        self.folder_name = folder_name
        self.create_new_folder()
        self.driver = driver
        self.url = url
        self.flights = []

    def create_new_folder(self):
        if not os.path.isdir(self.folder_name):
            os.mkdir(self.folder_name)

    def print_flights(self):
        for flight in self.flights:
            print(flight)

    def click_on_button(self):
        num_of_total_results = self.driver.find_element(By.XPATH, "//span[@id='totalItems']").get_attribute(
            'textContent')

        button = self.driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-primary rounded-pill js-load-more-flight-results']")
        while True:
            num_of_visible_results = self.driver.find_element(By.XPATH, "//span[@id='numOfResults']").get_attribute(
                'textContent')
            button[0].click()
            num_of_visible_results = self.driver.find_element(By.XPATH, "//span[@id='numOfResults']").get_attribute(
                'textContent')
            if num_of_total_results == num_of_visible_results:
                break
            button = self.driver.find_elements(By.XPATH,
                                               "//button[@class='btn btn-primary rounded-pill js-load-more-flight-results']")
        self.driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})

    def initiate_scraping(self):
        time.sleep(1)
        self.initiate_drive()
        time.sleep(1)
        self.click_on_button()
        time.sleep(1)
        self.scraping_rows()

    def in_list(self, obj):
        """
        :param obj: gets a flight object
        :return: if this object is inside list
        """
        key = (obj.flight_company + obj.flight + obj.terminal + obj.scheduled_time.replace('/', '').replace(':','')).replace(" ", "")

        for flight_object in self.flights:
            key_flight_object = (flight_object.flight_company + flight_object.flight + flight_object.terminal + flight_object.scheduled_time.replace('/', '').replace(':',
                                                                                                                '')).replace(
                " ", "")

            if key == key_flight_object:
                return True

    def scraping_rows(self):
        rows = self.driver.find_elements(By.XPATH, "//tr[@role='row']")

        for row in tqdm(rows):

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

            if self.in_list(flight_object):
                return
            if not flight_object.flight == '':
                self.flights.append(flight_object)
                print('added new flight')

    def save_object(self):
        save_list_of_obj(self.flights, self.folder_name)

    def load_objects(self):
        self.flights = load_list_of_json(self.folder_name)

    def update(self):

        self.driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})

        self.driver.refresh()
        time.sleep(10)

        button = self.driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-primary rounded-pill js-load-more-flight-results']")
        button[0].click()
        while True:
            self.flights = []
            self.driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})

            self.scraping_rows()

            self.driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})

            self.driver.refresh()
            time.sleep(10)

            button = self.driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-primary rounded-pill js-load-more-flight-results']")

            self.scraping_rows()

            self.save_object()

    def close_driver(self):
        self.driver.close()

    def initiate_drive(self):
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(2)

    def search_string_in_flight_list(self, string):
        list_of_relevant = []
        for obj in self.flights:
            if obj.string_in_object(string):
                list_of_relevant.append(obj)
        return list_of_relevant


