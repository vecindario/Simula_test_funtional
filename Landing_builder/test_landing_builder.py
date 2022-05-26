from selenium import webdriver
from Utils.WebFactory import WebDriverFactory
from Login.constanst import *
from Login.Loging import loggin
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, pytest
from Landing_builder.Landing_builder import buildercs
from selenium.common.exceptions import TimeoutException
from ddt import ddt, data, unpack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class test_users_agreements(unittest.TestCase):


    def test_agreements(self):
        wdriver = WebDriverFactory(NAVEGADOR)
        driver = wdriver.getWebDriverInstance()
        time.sleep(3)
        logging = loggin(driver)
        logging.loggIn_agreement()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        landingBuilder =buildercs(driver)
        landingBuilder.Click_landing()

