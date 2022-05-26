from selenium import webdriver
from Utils.WebFactory import WebDriverFactory
from Login.constanst import *
from Login.Loging import loggin
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from Create_Ptoject.CreateProject import CreateProjects
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, pytest
from selenium.common.exceptions import TimeoutException
from ddt import ddt, data, unpack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@ddt
class Createproject(unittest.TestCase):


    def test_sele(self):
        wdriver = WebDriverFactory(NAVEGADOR)
        driver = wdriver.getWebDriverInstance()
        time.sleep(3)
        logging = loggin(driver)
        logging.loggIn()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(5)
        myprojectnew = CreateProjects(driver)
        myprojectnew.CreatenewProject()








