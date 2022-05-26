
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Login.constanst import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ddt import ddt, data, unpack

class test_Asesor():

    def __init__(self, driver):
        self.driver = driver

    def Validations(self):
       elment = self.driver.find_element(By.XPATH,"/html/body/div/div/section/div/ul")
       elment.text
       print(elment)
       time.sleep(3)
       self.driver.find_element(By.XPATH,"tec")



    def Loginasesor(self):
        time.sleep(3)
        print(EMAIL)
        self.driver.find_element(By.NAME, "email").send_keys(EMAILASESOR)
        print(PASSEMAIL)
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(PASSEMAILASESOR)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-yellow')]").click()
        time.sleep(3)
        time.sleep(2)
        self.Validations()



