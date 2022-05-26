from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from CreateUser.createuser import testCreateuser
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, pytest
from ddt import ddt, data, unpack
from selenium import webdriver
from Utils.WebFactory import WebDriverFactory
from Login.constanst import *

@ddt
class Createproject(unittest.TestCase):


    def test_sele(self):
        driver = webdriver.Chrome()
        baseUrl = "https://simula-test-me:mwfbQeh4Qkp68oLQZ8mLsisbdE@pruebas.app.simula.vecindario.com/ingresar"
        driver.get(baseUrl)
        time.sleep(5)
        Mynewuser = testCreateuser(driver)
        Mynewuser.testsele()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        Mynewuser.createProject()
        Mynewuser.calendar()
        Mynewuser.datesingr()
        Mynewuser.Tipeinventary()


