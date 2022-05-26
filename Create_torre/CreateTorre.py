import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from API.testRials import testRial

import json
from random import randint, seed, random





class CreateTorre():

    def __init__(self, driver):
        self.driver = driver

    def case_startTorres(self):
        case = testRial()
        assert  "/crear-torre" in self.driver.current_url , case.updateCase('437', '5', 'Error no se encuentra la vista de crear proyecto')
        case.updateCase('437', '1', 'Succesfull')

    def case_fincreaciontorres(self):
        case = testRial()
        assert  "/selector-de-tipo" in self.driver.current_url , case.updateCase('438', '5', 'Error no se encuentra la vista de crear proyecto')
        case.updateCase('438', '1', 'Succesfull')


    def cratetorre(self):
        self.driver.find_element(By.XPATH, "(//a[@class='nav-link'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[@id='root']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/i[1]").click()
        time.sleep(4)
        self.case_startTorres()
        self.driver.find_element(By.NAME, "name").send_keys("AnamrilloAuto")


    def calendar(self):
        self.driver.find_element(By.XPATH,"(//label[text()='Fecha de entrega']/following::input)[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"(//div[@class='pika-label'])[1]").click()
        element2 = self.driver.find_element(By.XPATH,"//select[@class='pika-select pika-select-month']")
        sel = Select(element2)
        sel.select_by_value("6")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//div[@class='pika-label'])[2]").click()
        element3 = self.driver.find_element(By.XPATH, "//select[@class='pika-select pika-select-year']")
        sel1 = Select(element3)
        sel1.select_by_value("2022")
        calendar = self.driver.find_element(By.XPATH, "//table[@class='pika-table']/tbody[1]/tr[4]/td[6]")
        calendar.click()
        time.sleep(5)
    def datesingr(self):
        self.driver.find_element(By.XPATH,"(//input[@max='100'])[1]").send_keys("30")
        time.sleep(3)
        activeseparacion = "yes"
        if activeseparacion =="yes":
            self.driver.find_element(By.XPATH,"(//i[@class='fas fa-toggle-off'])[2]").click()
        time.sleep(1)
        activetasa= "yes"
        if activetasa == "yes":
            self.driver.find_element(By.XPATH,"//span[@class='toggle-activation text-right']//i[1]").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH,"(//input[@class='input-form form-control'])[3]").send_keys("5")
            time.sleep(2)
            self.driver.find_element(By.XPATH,"(//input[@class='input-form form-control'])[4]").send_keys("2")
            activapuntoeq = "no"
            if activapuntoeq == "yes":
                self.driver.find_element(By.XPATH,"//span[@class='toggle-activation ml-auto']//i[1]").click()
                self.driver.execute_script("window.scrollBy(0,500)")
                self.driver.find_element(By.XPATH,"(//label[text()='Fecha de punto de equilibrio:']/following::input)[1]").click()
                element3 = self.driver.find_element(By.XPATH, "(//select[@class='pika-select pika-select-month'])[2]")
                sel = Select(element3)
                sel.select_by_value("7")

                element4 = self.driver.find_element(By.XPATH, "(//select[@class='pika-select pika-select-year'])[2]")
                sel = Select(element4)
                sel.select_by_value("2022")
                calendar1 = self.driver.find_element(By.XPATH, "//table[@class='pika-table']/tbody[1]/tr[1]/td[2]")
                time.sleep(3)
                calendar1.click()
        cuotaspersonalitys = "no"
        if cuotaspersonalitys== "no":
            self.driver.find_element(By.XPATH,"(//i[@class='fas fa-toggle-on'])[1]").click()
            time.sleep(2)
        coutasprimas ="no"
        if coutasprimas == "no":
            self.driver.find_element(By.XPATH,"(//span[@class='toggle-activation text-right']//i)[4]").click()
        cuotascesantias= "no"
        if cuotascesantias == "no":
            self.driver.find_element(By.XPATH,"(//span[@class='toggle-activation text-right']//i)[5]").click()

        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(3)
        tipevivi = "Vip"
        time.sleep(3)
        if tipevivi == "Vip":
            self.driver.find_element(By.ID,"tower_type_vip").click()
            time.sleep(2)
            subsudy = self.driver.find_element(By.ID,"towerReceivesSubsidy")
            sel = Select(subsudy)
            sel.select_by_value("si")
            self.driver.execute_script("window.scrollBy(0,900)")
            self.driver.find_element(By.XPATH,"(//span[@class='toggle-activation ml-auto']//i)[2]").click()
            time.sleep(2)
            self.driver.find_element(By.NAME,"percentInInitialFee").send_keys("12")
            time.sleep(2)
        if tipevivi == "vis":
            self.driver.find_element(By.ID,"tower_type_vis").click()
            time.sleep(2)
            subsudy = self.driver.find_element(By.ID, "towerReceivesSubsidy")
            sel = Select(subsudy)
            time.sleep(3)
            sel.select_by_value("si")
            self.driver.execute_script("window.scrollBy(0,900)")
            self.driver.find_element(By.XPATH,"(//i[@class='fas fa-toggle-on'])[4]").click()
            time.sleep(2)
            self.driver.find_element(By.NAME, "percentInInitialFee").send_keys("12")
            time.sleep(2)
        if tipevivi == "novis":
            self.driver.find_element(By.ID,"tower_type_no_vis").click()
        time.sleep(2)


        plazoreu = self.driver.find_element(By.XPATH,"(//label[text()='Plazo de reutilización de simulaciones']/following::input)[1]")
        time.sleep(2)
        plazoreu.clear()
        plazoreu.send_keys("6")
        self.driver.execute_script("window.scrollBy(0,900)")

        #minblock = self.driver.find_element(By.XPATH, "(//input[@max='100'])[4]")
        #time.sleep(2)
        #time.sleep(2)
        #minblock.clear()
        #minblock.send_keys("15")

        mont = self.driver.find_element(By.XPATH,"(//input[@max='100'])[4]")
        time.sleep(3)
        mont.send_keys("15")
        time.sleep(2)
        state = self.driver.find_element(By.ID,"state")
        sel = Select(state)
        sel.select_by_value("in_build")
        time.sleep(2)
        self.driver.find_element(By.TAG_NAME,"textarea").send_keys("plazo de pagar cuota de 1-5 dias ")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text()='Siguiente']").click()
        time.sleep(5)
        self.case_fincreaciontorres()

    def Tipeinventary(self):
        Tipe = "parcial"
        if Tipe == "complete":
            self.driver.find_element(By.LINK_TEXT,"Inventario completo").click()
            time.sleep(6)
            filepath = "/home/mariana/Downloads/Simula+plantilla+inmuebles(2).xlsx"
            # self.driver.find_element(By.XPATH,"//div[@class='img-circle-ctn']//i[1]").click()c
            file_tag_list = self.driver.find_element(By.XPATH, "//input[@type='file']")
            file_tag_list.send_keys(filepath)
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,500)")
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//button[text()='Siguiente']").click()
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH,"//button[text()='Siguiente']").click()
            time.sleep(3)
        if Tipe == "parcial":
            self.driver.find_element(By.LINK_TEXT,"Inventario parcial").click()
            self.driver.find_element(By.XPATH,"//button[text()='Crear tipología']").click()
            filepath = "/home/mariana/Pictures/Screenshot from 2021-06-28 16-54-05.png"
            file_tag_list = self.driver.find_element(By.XPATH, "//input[@type='file']")
            file_tag_list.send_keys(filepath)
            self.driver.find_element(By.XPATH,"//button[text()='Confimar']").click()
            time.sleep(2)
            self.driver.find_element(By.NAME,"typology_name").send_keys("Tipo D")
            time.sleep(2)
            self.driver.find_element(By.XPATH,"(//button[@class='btn btn-yellow'])[2]").click()
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH,"//button[text()='Siguiente']").click()
            time.sleep(2)
            self.driver.find_element(By.NAME,"name").send_keys("Inmuble auto")
            self.driver.find_element(By.ID, "reference").send_keys("101")
            time.sleep(2)
            self.driver.find_element(By.ID, "private_meters").send_keys("101")
            self.driver.find_element(By.ID, "build_meters").send_keys("151")
            elementdis = self.driver.find_element(By.ID, "availability")
            sel = Select(elementdis)
            sel.select_by_value("available")
            self.driver.find_element(By.ID, "bedrooms").send_keys("2")
            self.driver.execute_script("window.scrollBy(0,700)")
            self.driver.find_element(By.ID, "bathrooms").send_keys("2")
            self.driver.find_element(By.ID, "bedrooms_option").send_keys("1")
            self.driver.find_element(By.ID, "bathrooms_option").send_keys("1")
            self.driver.find_element(By.ID, "floor").send_keys("5")
            acabados = self.driver.find_element(By.ID, "finishes_name")
            sel = Select(acabados)
            sel.select_by_value("Obra negra")
            self.driver.find_element(By.ID, "finishes_description").send_keys("El apto se entrega en obra negra y con puertas y ventanas")
            time.sleep(2)
            self.driver.find_element(By.ID, "base_price").send_keys("1500000000")
            self.driver.find_element(By.ID, "sight_bonus").send_keys("1000000")
            self.driver.find_element(By.ID, "discount_voucher").send_keys("900000")
            time.sleep(2)
            reservations  = self.driver.find_element(By.ID,"booking_value")
            reservations.send_keys("0")


            self.driver.find_element(By.ID, "height_bonus").send_keys("1000000")
            time.sleep(2)
            self.driver.find_element(By.NAME, "separation_value").send_keys("5000000")
            separations = self.driver.find_element(By.ID, "separation_value_included")
            time.sleep(2)
            sel = Select(separations)
            sel.select_by_value("true")
            self.driver.execute_script("window.scrollBy(0,700)")
            time.sleep(2)
            self.driver.find_element(By.XPATH,"(//div[contains(@class,'toggle__container ml-2')])[1]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//div[contains(@class,'toggle__container ml-2')])[2]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//button[text()='Guardar y continuar']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[text()='Siguiente Paso']").click()
            time.sleep(5)






        extras = "yes"
        if extras == "yes":
            self.driver.find_element(By.XPATH,"(//button[@class='btn btn-yellow'])[2]").click()
            self.driver.find_element(By.XPATH,"(//i[@class='far fa-plus'])[1]").click()
            tipeparq = self.driver.find_element(By.NAME,"type")
            sel = Select(tipeparq)
            sel.select_by_value("single")
            self.driver.find_element(By.TAG_NAME,"input").send_keys("10000000")
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH,"(//i[@class='far fa-plus'])[2]").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH,"(//input[@class='form-control mb-3'])[1]").send_keys("12333")
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[2]").send_keys("78")
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[3]").send_keys("Cueratoutilbajo")
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH,"//button[text()='Siguiente']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//i[@class='far fa-plus']").click()
            self.driver.find_element(By.XPATH,"(//input[@class='form-control mb-3'])[1]").send_keys("Piso")
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[2]").send_keys("1230")
            self.driver.find_element(By.TAG_NAME,"label").click()
            self.driver.find_element(By.XPATH,"//button[contains(@class,'mt-3 btn')]").click()
            self.driver.find_element(By.XPATH,"//button[text()='Siguiente']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//button[text()='Finalizar creación']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,"//button[text()='Ver simulador']").click()
            time.sleep(6)
















