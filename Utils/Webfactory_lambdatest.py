from selenium import webdriver
from Utils.constants import  *


class Webfactory_lambdaTest():

    def __init__(self, cap):
        self.cap = cap

    def getWebDriverInstance(self):
        try:
            print("start webdriver")
            print(self.cap)
            url = "https://" + username_lbtest + ":" + accessToken_lbtest + "@" + gridUrl_lbtest
            driver = webdriver.Remote(
                desired_capabilities=self.cap,
                command_executor=url
            )
            driver.implicitly_wait(3)
            driver.maximize_window()
            driver.get(BASEURL)
            return driver
        except Exception:
            raise Exception("Unable to load google page!")
