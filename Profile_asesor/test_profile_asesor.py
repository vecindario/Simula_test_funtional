from selenium import webdriver
from Utils.WebFactory import WebDriverFactory
from Login.constanst import *
from Login.Loging import loggin
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from Profile_asesor.profileAsesor import test_Asesor
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
class Test_aseor(unittest.TestCase):


    def test_profile_ase(self):
        wdriver = WebDriverFactory(NAVEGADOR)
        driver = wdriver.getWebDriverInstance()
        profile = test_Asesor(driver)
        profile.Loginasesor()

