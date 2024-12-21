from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automationFramework.Base.BaseClass import BaseClass
from automationFramework.Utils.globalVariableReader import getValue


waitTimeout = getValue("waitTimeout")

class HomePage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyHomePageOpened(self):
        if self.driver.title != "":
            return True
        else:
            raise Exception("Sayfa yüklenirken bir hata oluştu.")


    def handleCookies(self):
        try:
            WebDriverWait(self.driver, waitTimeout).until(EC.element_to_be_clickable((By.ID,
                                                                                      "wt-cli-accept-all-btn"))).click()
        except:
            pass
