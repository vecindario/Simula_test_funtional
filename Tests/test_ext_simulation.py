from Tests.flows.simulation import Simulatios_externa
from selenium import webdriver
import unittest
from ddt import ddt
from Tests.utils.webFactory import WebDriverFactory
from Tests.configuration.utils import readConfigurationJson

@ddt
class Test_admin(unittest.TestCase):


    def test_admin(self):

        data = readConfigurationJson("ext_simulation")
        dataTest = data[0]
        wdriver = WebDriverFactory(dataTest["browser"], dataTest["path"])
        driver = wdriver.getWebDriverInstance()
        simulationsw = Simulatios_externa(driver, dataTest)
        simulationsw.selectType()
        simulationsw.sendCurrentConsumer()
        simulationsw.customization()
        simulationsw.subsydy()
        simulationsw.typePay()
        simulationsw.firstPay()
