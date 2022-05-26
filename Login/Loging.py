from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from constanst import *
class loggin():

    def __init__(self, driver):
        self.driver = driver

    def loggIn(self):
        time.sleep(5)
        try:
            time.sleep(3)
            print(EMAIL)
            self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
            print(PASSEMAIL)
            time.sleep(2)
            self.driver.find_element(By.NAME, "password").send_keys(PASSEMAIL)
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-yellow')]").click()
            time.sleep(3)
        except Exception:
            raise Exception("Unable to load google page! login !!!!")
    def loggIn_agreement(self):
        time.sleep(5)
        try:
            time.sleep(3)
            print(EMAIL)
            self.driver.find_element(By.NAME, "email").send_keys(EMAIL_agreement)
            print(PASSEMAIL)
            time.sleep(2)
            self.driver.find_element(By.NAME, "password").send_keys(PASSEMAIL_agreement)
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-yellow')]").click()
            time.sleep(3)
        except Exception:
            raise Exception("Unable to load google page! login !!!!")
