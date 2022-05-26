import time
from Login.constanst import *
import webdriver_manager.utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from API.testRials import testRial
import json
from random import randint, seed, random

class Simulations_project_agreement_CS():

    def __init__(self, driver):
        self.driver = driver

    def Activations_project(self):
        self.driver.find_element(By.XPATH,"(//a[@class='nav-link'])[1]").click()
        self.driver.execute_script("window.scrollBy(0,1500)")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[@data-testid='project-toggle-activation']//i[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text()='Editar']").click()
        time.sleep(3)

    def Integrations_Sinco_CRM(self):
        self.driver.find_element(By.XPATH, "(//a[@class='nav-link'])[5]").click()
        time.sleep(6)
        self.driver.execute_script("window.scrollBy(0,2200)")
        self.driver.find_element(By.XPATH,"//div[@class='integrations-container']//div[contains(@class,'sinco-erp-box')]//button[contains(@class,'btn')]").click()
        time.sleep(2)
        self.driver.find_element(By.TAG_NAME,"input").send_keys(URL_PRUEBA_SINCO)
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//button[text()='Activar']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//i[@class='fas fa-warehouse']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//button[text()='Continuar']").click()
        self.driver.find_element(By.XPATH,"(//i[@class='fas fa-building'])[5]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text()='Continuar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Finalizar']").click()
        time.sleep(7)
    def Integrations_Sinco_CRM_ERP(self):
        self.driver.find_element(By.CSS_SELECTOR,"div#root>div:nth-of-type(2)>section>div>div:nth-of-type(2)>div>div>div:nth-of-type(15)>div>div>div:nth-of-type(3)>button").click()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.driver.find_element(By.TAG_NAME,"input").send_keys(URL_PRUEBA_SINCO)
        self.driver.find_element(By.XPATH, "//button[text()='Activar']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//i[@class='fas fa-warehouse']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[text()='Continuar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fas fa-building'])[5]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Continuar']").click()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 50)
        email = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Finalizar']"))).click()
        print(email)

    def TOWER_SINCO(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"(//button[contains(@class,'btn btn-main')])[1]").click()
        time.sleep(5)

    def simulations_agreements(self):
        parentHandle = self.driver.current_window_handle
        print("parent handle :" + parentHandle)

        handles = self.driver.window_handles

        for handle in handles:
            print("handle " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print("Swiched to window :: " + handle)

    def show_simulations(self):
        self.driver.find_element(By.XPATH,"//span[text()='Ver Simulación']").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,700)")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,700)")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,700)")












