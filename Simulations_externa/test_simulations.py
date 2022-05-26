from selenium import webdriver
from Utils.WebFactory import WebDriverFactory
from Login.constanst import *
from Login.Loging import loggin
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from Simulations_externa.simulations import Simulatios_externa
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
class Test_admin(unittest.TestCase):


    def test_admin(self):
        baseUrl = "https://develop.app.simula.vecindario.com/preview/vecindario-living"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        simulationsw = Simulatios_externa(driver)
        simulationsw.simulaexterno1()
        simulationsw.datespersonal()
        simulationsw.perzonalization()
        simulationsw.subsydy()
        simulationsw.formadepago()
        simulationsw.cuotaini()

