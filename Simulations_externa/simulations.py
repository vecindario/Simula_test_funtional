import time
from selenium.webdriver.common.action_chains import ActionChains
import webdriver_manager.utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from API.testRials import testRial
import json
from selenium.webdriver.support.select import Select
from random import randint, seed, random
from Login.constanst import *
class Simulatios_externa():

    def __init__(self, driver):
        self.driver = driver


    def simulaexterno1(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)")
        print("pas0")
        #self.driver.find_element(By.XPATH, "(//button[text()='Simular'])[1]").click()
        time.sleep(4)
        simula = "TipoA"
        if simula == "TipoA":
            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//input[contains(@class,'btn btn-yellow')])[1]").click()
            time.sleep(2)

        if simula == "TipoB":
            self.driver.find_element(By.XPATH, "(//div[text()='Apartamento'])[2]").click()
            self.driver.find_element(By.XPATH, "(//input[contains(@class,'btn btn-yellow')])[2]").click()
            time.sleep(2)

        if simula == "TipoC":
            self.driver.find_element(By.XPATH, "(//div[contains(@class,'flex-fill px-4')])[3]").click()
            self.driver.find_element(By.XPATH, "(//input[contains(@class,'btn btn-yellow')])[3]").click()

    def datespersonal(self):

        self.driver.find_element(By.NAME,"name").send_keys("Mariana andrea")
        self.driver.find_element(By.NAME, "lastname").send_keys("Lemus gil")
        selectyedocument = Select(self.driver.find_element_by_name('documentType'))
        time.sleep(2)
        selectyedocument.select_by_value("CC")
        time.sleep(2)
        self.driver.find_element(By.NAME,"documentNumber").send_keys("1030605587")
        time.sleep(1)
        self.driver.find_element(By.ID, "mobile").send_keys("3132991213")
        self.driver.find_element(By.NAME, "email").send_keys("qa.testing@vecindario.com")
        time.sleep(3)
        subsidy = Confirmacion
        if subsidy == "yes":
            self.driver.find_element(By.NAME,"dataPolicyCheck").click()
            time.sleep(2)
            self.driver.find_element(By.NAME,"financialCenterCheck").click()
            time.sleep(2)
        if subsidy == "no":
            self.driver.find_element(By.NAME, "dataPolicyCheck").click()
            time.sleep(2)

        self.driver.find_element(By.ID,"download-simulation").click()
        time.sleep(7)

    def perzonalization(self):

        personna  = "acabado"

        if personna == "parqueadero":
            self.driver.find_element(By.XPATH,"(//i[contains(@class,'ml-4 right')])[1]").click()
            select = Select(self.driver.find_element_by_id('select-parking-additions'))
            time.sleep(2)
            select.select_by_value("3000000")
            time.sleep(2)
        if personna == "cuertoutil":
            self.driver.find_element(By.XPATH,"(//i[contains(@class,'ml-4 right')])[2]").click()
            select = Select(self.driver.find_element_by_id('select-parking-additions'))
            select.select.select_by_value("45000000")
            time.sleep(2)

        if  personna == "acabado":
            self.driver.find_element(By.XPATH, "(//i[contains(@class,'ml-4 right')])[3]").click()
            time.sleep(2)
            select = Select(self.driver.find_element_by_name('finish'))
            select.select_by_visible_text("Ninguno")

        self.driver.find_element(By.XPATH,"(//button[@class='btn btn-yellow'])[2]").click()
        time.sleep(5)

    def subsydy(self):
        variable = "yes"
        if variable == "yes":
            select = Select(self.driver.find_element_by_id('apply_subsidy'))
            time.sleep(2)
            select.select_by_value("si")
            time.sleep(3)
            self.driver.find_element(By.ID,"family_income").send_keys("2000000")
            select1 = Select(self.driver.find_element_by_id('already_has_home'))
            time.sleep(2)
            select1.select_by_value("si")
            select2 = Select(self.driver.find_element_by_id('already_has_subsidy'))
            time.sleep(2)
            select2.select_by_value("si")
            select3 = Select(self.driver.find_element_by_id('compensation_fund'))
            time.sleep(2)
            select3.select_by_value("si")
            time.sleep(2)
            self.driver.find_element(By.ID,"compensation_fund_name").send_keys("230000000")
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH,"(//button[@class='btn btn-yellow'])[2]").click()
            time.sleep(2)

    def formadepago(self):
        cesan= "no"

        if cesan == "yes":
            self.driver.find_element(By.XPATH,"(//label[@name='yes-savings'])[1]").click()
            self.driver.find_element(By.XPATH,"(//input[@type='tel'])[1]").send_keys("18000000")
            drog = self.driver.find_element(By.XPATH, "(//div[@role='slider'])[1]")


            actions = ActionChains(self.driver)
            actions.click_and_hold(drog).move_by_offset(0, 0).release().perform()
            time.sleep(5)

        if cesan == "no":
            self.driver.find_element(By.NAME,"no-savings").click()
        self.driver.execute_script("window.scrollBy(0,500)")

    def cuotaini(self):
        self.driver.find_element(By.XPATH,"(//label[@name='yes-savings'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//h2[text()='Agregar Primas:']/following-sibling::div").click()
        # input1 = self.driver.find_element(By.XPATH, "(//input[@name='currency'])[1]")
        # input1.clear()
        # input1.send_keys("6500000")

        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)")
        # self.driver.find_element(By.XPATH, "(//input[@name='currency'])[2]").send_keys("200000000")
        time.sleep(1)
        # self.driver.find_element(By.XPATH, "(//input[@name='currency'])[3]").send_keys("300000000")
        self.driver.find_element(By.XPATH, "//h2[text()='Agregar Cesantías:']/following-sibling::div").click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH, "(//input[@name='currency'])[4]").send_keys("400000000")
        self.driver.find_element(By.XPATH,"//h2[text()='Agregar Cuotas personalizadas:']/following-sibling::div").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "currency").send_keys("500000000")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,700)")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Próximo paso']").click()
        #slider = self.driver.find_element(By.XPATH, "(//div[@role='slider'])[2]")
        #versions = ActionChains(self.driver)
        #versions.click_and_hold(slider).move_by_offset(10, 0).release().perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Generar Simulación']").click()
        time.sleep(7)

