from selenium import webdriver
from Utils.WebFactory import WebDriverFactory
from Login.constanst import *
from Login.Loging import loggin
from Create_Ptoject.CreateProject import CreateProjects
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from Silmulation_agreement_CS.SimulatiosProjectCS import Simulations_project_agreement_CS
from selenium.webdriver.common.by import By
from Simulations_externa.simulations import Simulatios_externa
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, pytest
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
        myprojectnew = CreateProjects(driver)
        myprojectnew.CreatenewProject()
        agremment = Simulations_project_agreement_CS(driver)
        agremment.Activations_project()
        agremment.Integrations_Sinco_CRM()
        agremment.Integrations_Sinco_CRM_ERP()
        agremment.TOWER_SINCO()
        agremment.simulations_agreements()
        simulatons =Simulatios_externa(driver)
        simulatons.simulaexterno1()
        simulatons.datespersonal()
        simulatons.formadepago()
        simulatons.cuotaini()
        agremment.show_simulations()
