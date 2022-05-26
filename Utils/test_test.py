from CreateUser.createuser import testCreateuser
from Utils.WebFactory import WebDriverFactory
from constants import *
from Webfactory_browsersatck import Webfactory_browsersatck
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from Login.Loging import loggin
from Create_Ptoject.CreateProject import CreateProjects
from constants import *
import time
from Login.constanst import *
import unittest, pytest
from ddt import ddt, data, unpack
@ddt
class Creates(unittest.TestCase):
  wdriver = WebDriverFactory(NAVEGADOR)
  driver = wdriver.getWebDriverInstance()
  time.sleep(5)
  Mynewuser = testCreateuser(driver)
  Mynewuser.testsele()
  webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
  Mynewuser.createProject()
  Mynewuser.calendar()
  Mynewuser.datesingr()
  Mynewuser.Tipeinventary()

  print(driver.title)
  print("fin")
  driver.quit()


#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly




