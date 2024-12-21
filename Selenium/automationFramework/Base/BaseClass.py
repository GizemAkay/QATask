import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from automationFramework.Utils.globalVariableReader import getValue
from automationFramework.Utils.locator import getLocator

waitTimeout = getValue("waitTimeout")


@pytest.mark.xfail(raises=Exception, strict=True)
class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    # Verify if the element is located in the page if not raise exception
    def verifyItemInPage(self, item=None, section=None):
        try:
            xpath = getLocator(item, section)
            verifiedItem = WebDriverWait(self.driver, waitTimeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))).text.strip()
            if not verifiedItem:
                raise Exception(f"Elementin sayfada olduğu doğrulanamadı'")
            return verifiedItem
        except Exception as e:
            raise Exception(f"Elementin sayfada olduğu doğrulanamadı'{e}")
