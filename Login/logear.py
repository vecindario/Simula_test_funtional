from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

from Login.Loging import loggin

from Login.constanst import *
from Utils.WebFactory import WebDriverFactory
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logging
import Utils.costum_logger as cl

class FindByClassTag():
    log = cl.customLogger(logging.DEBUG)

    def test(self):
        #try:

        wdriver = WebDriverFactory(NAVEGADOR)
        driver = wdriver.getWebDriverInstance()
        logging = loggin(driver)
        logging.loggIn()





    # except Exception:
        #    self.log.error("### Error en el test - " + ID_CASO_TEST)


vecindario = FindByClassTag()
vecindario.test()