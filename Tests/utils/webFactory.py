from selenium import webdriver
import logging
import Utils.costum_logger as cl


class WebDriverFactory():

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, browser, path):
        self.browser = browser
        self.path = path

    def getWebDriverInstance(self):
        try:
            if self.browser == "iexplorer":
                self.log.warning("### Navegador no soportado")
            elif self.browser == "firefox":
                driver = webdriver.Firefox()
            elif self.browser == "chrome":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Chrome()
            driver.implicitly_wait(3)
            driver.maximize_window()
            driver.get(self.path)
            return driver
        except Exception:
            self.log.error("### Error al obtener el driver")
