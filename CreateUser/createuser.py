
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ddt import ddt, data, unpack

class testCreateuser():

    def __init__(self, driver):
        self.driver = driver


    def testsele(self):
        self.driver.find_element(By.LINK_TEXT,"Crea una cuenta").click()
        time.sleep(2)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("name").send_keys("Prueba")
        time.sleep(3)
        self.driver.find_element_by_id("mobile").send_keys("3205041677")
        time.sleep(3)
        self.driver.find_element_by_id("email").send_keys("pruba3456@gmail.com")
        time.sleep(3)
        self.driver.find_element_by_id("password").send_keys("abc123452")
        time.sleep(13)
        self.driver.find_element_by_id("passwordConfirmation").send_keys("abc123452")
        time.sleep(13)
        element = self.driver.find_element_by_class_name('custom-control-input')
        self.driver.execute_script("arguments[0].click();", element)

        self.driver.find_element_by_xpath("//button[contains(@class,'btn-register btn')]").click()
        time.sleep(5)

    def createProject(self):
        self.driver.find_element(By.NAME, "title").send_keys("Proyecto amarillo")
        time.sleep(2)
        self.driver.find_element(By.NAME, "company_name").send_keys("Corona")
        TipoProject = "Comercial"
        if TipoProject == "Comercial":
            self.driver.find_element(By.XPATH, "//input[@value='commercial']").click()
            time.sleep(1)
        if TipoProject == "Residencial":
            self.driver.find_element(By.XPATH, "//input[@value='residential']").click()
            time.sleep(1)
        if TipoProject == "Mixto":
            self.driver.find_element(By.XPATH, "(//div[@class='flex-ctn cards-ctn']//div)[5]")
        EstadoProjec = "Sobreplanos"

        if EstadoProjec == "Estruct":
            self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/fieldset[1]/div[1]/div[1]").click()
            time.sleep(1)

        if EstadoProjec == "Sobreplanos":
            self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/fieldset[1]/div[1]/div[2]").click()
            time.sleep(1)
        if EstadoProjec == "construccion":
            self.driver.find_element(By.XPATH,"//div[@id='root']/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/fieldset[1]/div[1]/div[3]").click()
            time.sleep(1)
        if EstadoProjec == "Entregainmediata":
            self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/fieldset[1]/div[1]/div[3]").click()
            time.sleep(1)

        self.driver.find_element(By.NAME, "data_authorization").send_keys( "https://www.aepd.es/es/politica-de-privacidad-y-aviso-legal")
        time.sleep(2)
        self.driver.find_element(By.NAME, "expire_simulation_time").send_keys("30")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-dimgray')])[1]").click()
        time.sleep(5)
        city = self.driver.find_element(By.NAME, "project_city")
        city.send_keys("Medellín, Antioquia, Colombia")
        city.send_keys(Keys.DOWN)
        city.send_keys(Keys.ENTER)
        self.driver.find_element(By.NAME, "project_address").send_keys("Calle 122")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
        time.sleep(1)
        filepath = "/home/mariana/Pictures/Screenshot from 2021-06-23 17-35-54.png"
        # self.driver.find_element(By.XPATH,"//div[@class='img-circle-ctn']//i[1]").click()c
        file_tag_list = self.driver.find_element(By.XPATH, "//input[@type='file']")
        file_tag_list.send_keys(filepath)
        self.driver.find_element(By.XPATH, "//button[text()='Confimar']").click()
        self.driver.execute_script("window.scrollBy(0,500)")
        self.driver.find_element(By.XPATH, "//button[text()='Agrega inventario']").click()
        time.sleep(4)



    def calendar(self):
        self.driver.find_element(By.NAME, "name").send_keys("AnamrilloAuto")
        self.driver.find_element(By.XPATH, "(//label[text()='Fecha de entrega']/following::input)[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//div[@class='pika-label'])[1]").click()
        element2 = self.driver.find_element(By.XPATH, "//select[@class='pika-select pika-select-month']")
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
        self.driver.find_element(By.XPATH, "(//input[@max='100'])[1]").send_keys("30")
        time.sleep(3)
        activetasa = "yes"
        if activetasa == "yes":
            self.driver.find_element(By.XPATH, "//span[@class='toggle-activation text-right']//i[1]").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "(//input[@class='input-form form-control'])[3]").send_keys("5")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//input[@class='input-form form-control'])[4]").send_keys("2")
            activapuntoeq = "no"
            if activapuntoeq == "yes":
                self.driver.find_element(By.XPATH, "//span[@class='toggle-activation ml-auto']//i[1]").click()
                self.driver.execute_script("window.scrollBy(0,500)")
                self.driver.find_element(By.XPATH,
                                         "(//label[text()='Fecha de punto de equilibrio:']/following::input)[1]").click()
                element3 = self.driver.find_element(By.XPATH, "(//select[@class='pika-select pika-select-month'])[2]")
                sel = Select(element3)
                sel.select_by_value("7")

                element4 = self.driver.find_element(By.XPATH, "(//select[@class='pika-select pika-select-year'])[2]")
                sel = Select(element4)
                sel.select_by_value("2022")
                calendar1 = self.driver.find_element(By.XPATH, "//table[@class='pika-table']/tbody[1]/tr[1]/td[2]")
                time.sleep(3)
                calendar1.click()
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(3)
        tipevivi = "Vip"
        time.sleep(3)
        if tipevivi == "Vip":
            self.driver.find_element(By.ID, "tower_type_vip").click()
            time.sleep(2)
            subsudy = self.driver.find_element(By.ID, "towerReceivesSubsidy")
            sel = Select(subsudy)
            sel.select_by_value("si")
            self.driver.execute_script("window.scrollBy(0,900)")
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/section/div/div/div/div[1]/div[1]/form/div[11]/div/span/i").click()
            time.sleep(2)
            self.driver.find_element(By.NAME, "percentInInitialFee").send_keys("12")
            time.sleep(2)
        if tipevivi == "vis":
            self.driver.find_element(By.ID, "tower_type_vis").click()
            time.sleep(2)
            subsudy = self.driver.find_element(By.ID, "towerReceivesSubsidy")
            sel = Select(subsudy)
            time.sleep(3)
            sel.select_by_value("si")
            self.driver.execute_script("window.scrollBy(0,900)")
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/section/div/div/div/div[1]/div[1]/form/div[11]/div/span/i").click()
            time.sleep(2)
            self.driver.find_element(By.NAME, "percentInInitialFee").send_keys("12")
            time.sleep(2)
        if tipevivi == "novis":
            self.driver.find_element(By.ID, "tower_type_no_vis").click()
        mont = self.driver.find_element(By.XPATH, "//label[text()='Plazo cuota inicial:']/following::input")
        time.sleep(3)
        mont.send_keys(Keys.UP)
        time.sleep(2)
        state = self.driver.find_element(By.ID, "state")
        sel = Select(state)
        sel.select_by_value("in_build")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Siguiente']").click()
        time.sleep(5)

    def Tipeinventary(self):
        Tipe = "complete"
        if Tipe == "complete":
            self.driver.find_element(By.LINK_TEXT, "Inventario completo").click()
            time.sleep(6)
            filepath = "/home/mariana/Downloads/Simula+plantilla+inmuebles(2).xlsx"
            # self.driver.find_element(By.XPATH,"//div[@class='img-circle-ctn']//i[1]").click()c
            file_tag_list = self.driver.find_element(By.XPATH, "//input[@type='file']")
            file_tag_list.send_keys(filepath)
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,500)")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[text()='Siguiente']").click()
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH, "//button[text()='Siguiente']").click()
            time.sleep(3)
        if Tipe == "parcial":
            self.driver.find_element(By.LINK_TEXT, "Inventario parcial").click()
            self.driver.find_element(By.XPATH, "//button[text()='Crear tipología']").click()
            filepath = "/home/mariana/Pictures/Screenshot from 2021-06-28 16-54-05.png"
            file_tag_list = self.driver.find_element(By.XPATH, "//input[@type='file']")
            file_tag_list.send_keys(filepath)
            self.driver.find_element(By.XPATH, "//button[text()='Confimar']").click()
            time.sleep(2)
            self.driver.find_element(By.NAME, "typology_name").send_keys("Tipo D")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//button[@class='btn btn-yellow'])[2]").click()
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH, "//button[text()='Siguiente']").click()

        extras = "yes"
        if extras == "yes":
            self.driver.find_element(By.XPATH, "(//button[@class='btn btn-yellow'])[2]").click()
            self.driver.find_element(By.XPATH, "(//i[@class='far fa-plus'])[1]").click()
            tipeparq = self.driver.find_element(By.NAME, "type")
            sel = Select(tipeparq)
            sel.select_by_value("single")
            self.driver.find_element(By.TAG_NAME, "input").send_keys("10000000")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "(//i[@class='far fa-plus'])[2]").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[1]").send_keys("12333")
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[2]").send_keys("78")
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[3]").send_keys("Cueratoutilbajo")
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,500)")
            self.driver.find_element(By.XPATH, "//button[text()='Siguiente']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//i[@class='far fa-plus']").click()
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[1]").send_keys("Piso")
            self.driver.find_element(By.XPATH, "(//input[@class='form-control mb-3'])[2]").send_keys("1230")
            self.driver.find_element(By.XPATH, "//label[text()='A']").click()
            self.driver.find_element(By.XPATH, "//button[contains(@class,'mt-3 btn')]").click()
            self.driver.find_element(By.XPATH, "//button[@class='btn btn-yellow']").click()
            time.sleep(2)
            self.driver.find_element(By.LINK_TEXT, "Finalizar").click()
            time.sleep(3)




