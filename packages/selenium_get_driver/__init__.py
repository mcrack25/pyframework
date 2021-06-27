import os
from selenium import webdriver

class GetDriver:
    driver = None

    def __init__(self, driver_path, browser):
        if browser == 'firefox':
            driver = webdriver.Firefox(executable_path=driver_path)
        elif browser == 'chrome':
            driver = webdriver.Chrome(executable_path=driver_path)
        else:
            driver = None

        self.driver = driver

    def get(self):
        return self.driver