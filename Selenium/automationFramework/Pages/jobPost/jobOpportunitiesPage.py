from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automationFramework.Base.BaseClass import BaseClass
from automationFramework.Utils.locator import getLocator
from automationFramework.Utils.globalVariableReader import getValue

waitTimeout = getValue("waitTimeout")


class JobOpportunitiesPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def returnCountersText(self):
        counter = WebDriverWait(self.driver, waitTimeout).until(
            EC.visibility_of_element_located((By.XPATH, getLocator("counter", "QA"))))
        return counter.text

    def countJobOpportunities(self):
        jobOpportunities = WebDriverWait(self.driver, waitTimeout).until(
            EC.presence_of_all_elements_located((By.XPATH, getLocator("viewRole", "QA"))))
        return len(jobOpportunities)
