from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Login.constanst import *
import logging
import Utils.costum_logger  as cl


class WebDriverFactory():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        try:
            if self.browser == "iexplorer":
                self.log.warning("### Navegador no soportado")
                # cap = DesiredCapabilities().INTERNETEXPLORER
                # cap['ignoreZoomSetting'] = True
                # driver = webdriver.Ie(capabilities=cap, executable_path=r'd:\\IEDriver\\IEDriverServer.exe')
            elif self.browser == "firefox":
                driver = webdriver.Firefox()
            elif self.browser == "chrome":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Chrome()

            driver.implicitly_wait(3)
            driver.maximize_window()
            driver.get(BASEURL)
            return driver
        except Exception:
            self.log.error("### Error al obtener el driver")
