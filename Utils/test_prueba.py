from threading import Thread
import os
from time import sleep
from constants import *
from Webfactory_browsersatck import Webfactory_browsersatck
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Login.Loging import loggin
from Create_Ptoject.CreateProject import CreateProjects
import time
import unittest, pytest
from ddt import ddt, data, unpack
# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run


#run_session function searches for 'BrowserStack' on google.com
def test_run_session(cap):

  try:
    wdriver = Webfactory_browsersatck(cap)
    driver = wdriver.getWebDriverInstance()
    logging = loggin(driver)
    logging.loggIn()
    time.sleep(5)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(5)
    myprojectnew = CreateProjects(driver)
    myprojectnew.CreatenewProject()
  except TimeoutException:
    driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched 2" }}')
  except Exception:
    driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Login  not matched 2" }}')
  print(driver.title)
  print("fin")
  driver.quit()

#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly




