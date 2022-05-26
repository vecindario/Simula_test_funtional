import time

import webdriver_manager.utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from API.testRials import testRial
import json
from Login.constanst import *
from random import randint, seed, random





class CreateProjects():

    def __init__(self, driver):
        self.driver = driver

    def case_startProject(self):
        try:
            print(self.driver.current_url)
            print("ssssssssssssssssssssssssssssssssssssssss")
            case = testRial()
            assert "https://develop.app.simula.vecindario.com/guia/crear-proyecto" in self.driver.current_url, case.updateCase('402','5', 'Error no se encuentra la vista de crear proyecto')
            case.updateCase('402', '1', 'Succesfull')
        except NameError :
            print(NameError)

    def case_startProject1(self):
        case = testRial()
        assert  "/proyectos" in self.driver.current_url , case.updateCase('403', '5', 'Error no se encuentra la vista de crear proyecto')
        case.updateCase('403', '1', 'Succesfull')

    def CreatenewProject(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "mr-2").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div/div[2]/nav/div/ul[1]/li/div/div/ul/li[1]").click()
            time.sleep(6)
            self.case_startProject()
            self.driver.find_element(By.NAME, "title").send_keys(NAME_PROJECT)
            time.sleep(2)
            self.driver.find_element(By.NAME, "company_name").send_keys(COMPANY_NAME)
            time.sleep(3)
            TipoProject = TYPE_PROJECT
            if TipoProject == "Comercial":
                self.driver.find_element(By.XPATH, "//input[@value='commercial']").click()
                time.sleep(1)
            if TipoProject == "Residencial":
                self.driver.find_element(By.XPATH, "//input[@value='residential']").click()
                time.sleep(1)
            if TipoProject == "Mixto":
                self.driver.find_element(By.XPATH, "(//div[@class='flex-ctn cards-ctn']//div)[5]")

            EstadoProjec = STATE_PROJECT
            time.sleep(2)
            if EstadoProjec == "Estruct":
                self.driver.find_element(By.XPATH,"//div[@id='root']/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/fieldset[1]/div[1]/div[1]").click()
                time.sleep(1)
            if EstadoProjec == "Sobreplanos":
                self.driver.find_element(By.XPATH,"//div[@id='root']/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/fieldset[1]/div[1]/div[2]").click()
                time.sleep(1)
            if EstadoProjec == "construccion":
                self.driver.find_element(By.XPATH,"//input[@data-testid='on_plans-id']").click()
                time.sleep(1)
            if EstadoProjec == "Entregainmediata":
                self.driver.find_element(By.XPATH,"//div[@id='root']/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/fieldset[1]/div[1]/div[3]").click()
                time.sleep(1)

            self.driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-dimgray')])[1]").click()
            time.sleep(5)
            city = self.driver.find_element(By.NAME, "project_city")
            city.send_keys(CITY)
            city.send_keys(Keys.DOWN)
            city.send_keys(Keys.ENTER)
            self.driver.find_element(By.NAME, "project_address").send_keys(PROJECT_ADRESS)
            time.sleep(1)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
            time.sleep(2)

            self.driver.execute_script("window.scrollBy(0,700)")
            self.driver.find_element(By.NAME, "data_authorization").send_keys(AUTORIZACION_DATA)
            time.sleep(2)
            self.driver.find_element(By.NAME, "expire_simulation_time").send_keys(TIME_SIMULATIONS_EXPIRE)
            time.sleep(1)
            filepath = LOGO_PROJECT
            # self.driver.find_element(By.XPATH,"//div[@class='img-circle-ctn']//i[1]").click()c
            file_tag_list = self.driver.find_element(By.XPATH, "//input[@type='file']")
            file_tag_list.send_keys(filepath)
            self.driver.find_element(By.XPATH, "//button[text()='Confimar']").click()
            print("sssss")
            self.driver.find_element(By.XPATH, "//button[text()='Finaliza proyecto']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,"//button[text()='si, seguro']").click()
            time.sleep(6)
            print(self.driver.current_url)
            self.case_startProject1()
            time.sleep(6)

        except NameError:
            print(NameError)




