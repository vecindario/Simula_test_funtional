from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from constants import *

class Webfactory_browsersatck():

    def __init__(self, cap):
        self.cap = cap

    def getWebDriverInstance(self):
        try:
            print("inicio ")
            driver = webdriver.Remote(
                command_executor='https://marianalemus_iW57Zn:GybqKJKi2WfjWBfpfaa7@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities=self.cap)
            driver.implicitly_wait(3)
            driver.maximize_window()
            driver.get(BASEURL)
            return driver
        except Exception:
            raise Exception("Unable to load google page!")
