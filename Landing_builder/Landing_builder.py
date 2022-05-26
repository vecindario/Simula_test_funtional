import time
from Login.constanst import *
import webdriver_manager.utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from API.testRials import testRial
import json
from random import randint, seed, random

class buildercs():

    def __init__(self, driver):
        self.driver = driver

    def Click_landing(self):
        self.driver.find_element(By.XPATH, "(//a[@class='nav-link'])[5]").click()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.driver.find_element(By.XPATH,"//button[text()='Crear']").click()
        time.sleep(2)