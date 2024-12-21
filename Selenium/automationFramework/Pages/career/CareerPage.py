import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automationFramework.Base.BaseClass import BaseClass
from automationFramework.Utils.globalVariableReader import getValue
from automationFramework.Utils.locator import getLocator

waitTimeout = getValue("waitTimeout")


class CareerPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def openCareersPage(self):
        WebDriverWait(self.driver, waitTimeout).until(EC.presence_of_element_located((By.XPATH, getLocator("company",
                                                                                                       "HomePage")))).click()
        WebDriverWait(self.driver, waitTimeout).until(EC.presence_of_element_located((By.XPATH, getLocator("careers",
                                                                                                       "HomePage")))).click()
