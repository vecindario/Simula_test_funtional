import time

import webdriver_manager.utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from API.testRials import testRial
import json
from selenium.webdriver.support.select import Select
from random import randint, seed, random
from Login.constanst import *
class CreateUserAdmin():

    def __init__(self, driver):
        self.driver = driver
    def Directorconfir(self):
        dire = self.driver.find_element(By.XPATH, "(//button[contains(@class,'position-relative btn-rol')])[2]").text

        assert "director" == dire
    def add_users_director(self):
        self.driver.find_element(By.XPATH, "(//a[@class='nav-link'])[4]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()='Agregar usuario']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@data-testid='email-field']").send_keys("director1122@vecindario.com")
        Rol = self.driver.find_element(By.ID, "rol")
        sel = Select(Rol)
        sel.select_by_value("director")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@class='form-control mb-4']").send_keys("mus22222")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)

    def add_user_Asesor(self):
        self.driver.find_element(By.XPATH, "//button[text()='Agregar usuario']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@data-testid='email-field']").send_keys("asesor1122@vecindario.com")
        Rol = self.driver.find_element(By.ID, "rol")
        sel = Select(Rol)
        sel.select_by_value("asesor")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@class='form-control mb-4']").send_keys("mus2222221")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
