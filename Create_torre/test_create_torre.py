
from selenium import webdriver
from Utils.WebFactory import WebDriverFactory
from Login.constanst import *
from Login.Loging import loggin
from selenium.webdriver.common.action_chains import ActionChains
from Create_Ptoject.CreateProject import CreateProjects
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Create_torre.CreateTorre import CreateTorre
from selenium.webdriver.support.ui import Select
import unittest, pytest
from ddt import ddt, data, unpack

@ddt
class CreatTorre(unittest.TestCase):


    def test_Torre(self):
        wdriver = WebDriverFactory(NAVEGADOR)
        driver = wdriver.getWebDriverInstance()
        logging = loggin(driver)
        logging.loggIn()
        time.sleep(5)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        torre = CreateTorre(driver)
        torre.cratetorre()
        torre.calendar()
        torre.datesingr()
        torre.Tipeinventary()
        time.sleep(2)

