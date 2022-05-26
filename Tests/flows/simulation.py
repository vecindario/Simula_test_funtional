import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Login.constanst import *
class Simulatios_externa():

    def __init__(self, driver, test):

        self.driver = driver
        self.test = test


    def selectType(self):

        time.sleep(self.test["sleep"] + 1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(self.test["sleep"] + 2)
        state = 1
        try:
            if self.test["type"] == "Type A":
                self.driver.find_element(By.XPATH, "(//input[contains(@class,'btn btn-yellow')])[1]").click()
                time.sleep(self.test["sleep"])
            elif self.test["type"] == "Type B":
                self.driver.find_element(By.XPATH, "(//div[text()='Apartamento'])[2]").click()
                self.driver.find_element(By.XPATH, "(//input[contains(@class,'btn btn-yellow')])[2]").click()
                time.sleep(self.test["sleep"])
            elif self.test["type"] == "Type C":
                self.driver.find_element(By.XPATH, "(//div[contains(@class,'flex-fill px-4')])[3]").click()
                self.driver.find_element(By.XPATH, "(//input[contains(@class,'btn btn-yellow')])[3]").click()
                time.sleep(self.test["sleep"])
        except:
            state = 0
            assert state == 1, print("Error in step selecType")

    def sendCurrentConsumer(self):

        state = 1
        try:
            self.driver.find_element(By.NAME,"name").send_keys(self.test["data"]["name"])
            self.driver.find_element(By.NAME, "lastname").send_keys(self.test["data"]["lastName"])
            selectyedocument = Select(self.driver.find_element_by_name('documentType'))
            time.sleep(self.test["sleep"])
            selectyedocument.select_by_value("CC")
            time.sleep(self.test["sleep"])
            self.driver.find_element(By.NAME,"documentNumber").send_keys(self.test["data"]["idUser"])
            time.sleep(self.test["sleep"])
            self.driver.find_element(By.ID, "mobile").send_keys(self.test["data"]["cell"])
            self.driver.find_element(By.NAME, "email").send_keys(self.test["data"]["email"])
            time.sleep(self.test["sleep"] + 1)
            subsidy = Confirmacion
            if subsidy == "yes":
                self.driver.find_element(By.NAME,"dataPolicyCheck").click()
                time.sleep(self.test["sleep"])
                self.driver.find_element(By.NAME,"financialCenterCheck").click()
                time.sleep(self.test["sleep"])
            elif subsidy == "no":
                self.driver.find_element(By.NAME, "dataPolicyCheck").click()
                time.sleep(self.test["sleep"])

            self.driver.find_element(By.ID,"download-simulation").click()
            time.sleep(self.test["sleep"] + 4)
        except:
            state = 0
            assert state == 1, print("Error in step sendCurrentConsumer")

    def customization(self):

        state = 1
        try:
            if self.test["data"]["custom"] == "parqueadero":
                self.driver.find_element(By.XPATH,"(//i[contains(@class,'ml-4 right')])[1]").click()
                select = Select(self.driver.find_element_by_id('select-parking-additions'))
                time.sleep(self.test["sleep"])
                select.select_by_value(self.test["parking"])
                time.sleep(self.test["sleep"])
            elif self.test["data"]["custom"] == "cuertoutil":
                self.driver.find_element(By.XPATH,"(//i[contains(@class,'ml-4 right')])[2]").click()
                select = Select(self.driver.find_element_by_id('select-parking-additions'))
                select.select.select_by_value(self.test["room"])
                time.sleep(self.test["sleep"])
            elif self.test["data"]["custom"] == "acabado":
                self.driver.find_element(By.XPATH, "(//i[contains(@class,'ml-4 right')])[3]").click()
                time.sleep(self.test["sleep"])
                select = Select(self.driver.find_element_by_name('finish'))
                select.select_by_visible_text("Ninguno")
            self.driver.find_element(By.XPATH,"(//button[@class='btn btn-yellow'])[2]").click()
            time.sleep(self.test["sleep"] + 3)
        except:
            state = 0
            assert state == 1, print("Error in step customization")

    def subsydy(self):

        state = 1
        try:
            if self.test["data"]["subsidy"] != None:
                select = Select(self.driver.find_element_by_id('apply_subsidy'))
                time.sleep(self.test["sleep"])
                select.select_by_value("si")
                time.sleep(self.test["sleep"])
                self.driver.find_element(By.ID,"family_income").send_keys(self.test["data"]["subsidyFamily"])
                select1 = Select(self.driver.find_element_by_id('already_has_home'))
                time.sleep(self.test["sleep"])
                select1.select_by_value("si")
                select2 = Select(self.driver.find_element_by_id('already_has_subsidy'))
                time.sleep(self.test["sleep"])
                select2.select_by_value("si")
                select3 = Select(self.driver.find_element_by_id('compensation_fund'))
                time.sleep(self.test["sleep"])
                select3.select_by_value("si")
                time.sleep(self.test["sleep"])
                self.driver.find_element(By.ID,"compensation_fund_name").send_keys(self.test["data"]["subsidy"])
                time.sleep(self.test["sleep"])
                self.driver.execute_script("window.scrollBy(0,500)")
                self.driver.find_element(By.XPATH,"(//button[@class='btn btn-yellow'])[2]").click()
                time.sleep(self.test["sleep"])
        except:
            state = 0
            assert state == 1, print("Error in step subsydy")

    def typePay(self):
        state = 1
        try:
            if self.test["data"]["cesan"] != None:
                self.driver.find_element(By.XPATH,"(//label[@name='yes-savings'])[1]").click()
                self.driver.find_element(By.XPATH,"(//input[@type='tel'])[1]").send_keys(self.test["data"]["cesan"])
                drog = self.driver.find_element(By.XPATH, "(//div[@role='slider'])[1]")
                actions = ActionChains(self.driver)
                actions.click_and_hold(drog).move_by_offset(0, 0).release().perform()
                time.sleep(self.test["sleep"] + 3)
            else:
                self.driver.find_element(By.NAME,"no-savings").click()
            self.driver.execute_script("window.scrollBy(0,500)")
        except:
            state = 0
            assert state == 1, print("Error in step typePay")


    def firstPay(self):

        state = 1
        try:
            # Valida - valor de la cuota
            cuota = self.driver.find_element(By.XPATH, "//div[contains(@class,'row-pay-simulation')]//span[contains(@class,'blue-bold-text')]").text
            assert cuota == "7000", print("Error in step firstPay - Cuota")

            time.sleep(self.test["sleep"] + 135)
            self.driver.find_element(By.XPATH,"(//label[@name='yes-savings'])[2]").click()
            time.sleep(self.test["sleep"])
            self.driver.find_element(By.XPATH, "//h2[text()='Agregar Primas:']/following-sibling::div").click()
            # input1 = self.driver.find_element(By.XPATH, "(//input[@name='currency'])[1]")
            # input1.clear()
            # input1.send_keys("6500000")

            time.sleep(self.test["sleep"])
            self.driver.execute_script("window.scrollBy(0,500)")
            # self.driver.find_element(By.XPATH, "(//input[@name='currency'])[2]").send_keys("200000000")
            time.sleep(self.test["sleep"])
            # self.driver.find_element(By.XPATH, "(//input[@name='currency'])[3]").send_keys("300000000")
            self.driver.find_element(By.XPATH, "//h2[text()='Agregar Cesantías:']/following-sibling::div").click()
            time.sleep(self.test["sleep"])
            # self.driver.find_element(By.XPATH, "(//input[@name='currency'])[4]").send_keys("400000000")
            #self.driver.find_element(By.XPATH, "//h2[text()='Agregar Cuotas personalizadas:']/following-sibling::div").click()
            time.sleep(self.test["sleep"])
            self.driver.find_element(By.NAME, "currency").send_keys("500000000")
            time.sleep(self.test["sleep"])
            self.driver.execute_script("window.scrollBy(0,700)")
            time.sleep(self.test["sleep"])
            self.driver.find_element(By.XPATH, "//button[text()='Próximo paso']").click()
            #slider = self.driver.find_element(By.XPATH, "(//div[@role='slider'])[2]")
            #versions = ActionChains(self.driver)
            #versions.click_and_hold(slider).move_by_offset(10, 0).release().perform()
            time.sleep(self.test["sleep"])
            self.driver.find_element(By.XPATH, "//button[text()='Generar Simulación']").click()
            time.sleep(self.test["sleep"] + 5)
        except:
            state = 0
            assert state == 1, print("Error in step firstPay")


