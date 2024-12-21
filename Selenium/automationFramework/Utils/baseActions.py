import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from automationFramework.Utils.globalVariableReader import getValue

waitTimeout = getValue("waitTimeout")
implicitWait = getValue("implicitWait")


def clickIfVisible(driver, element, locatorType=By.XPATH):
    try:
        driver.find_element(locatorType, element).click()

    except Exception:
        pass


def ifElementClickable(driver, xpath):
    try:
        WebDriverWait(driver, waitTimeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return True
    except Exception as e:
        return False

# Select an option from dropdown
def selectFromDropdown(driver, xpath, value):
    xpath = driver.find_element(By.XPATH, xpath)
    tries = 3
    while Select(xpath).first_selected_option.text != value:
        try:
            Select(xpath).select_by_value(value)
        except Exception:
            try:
                Select(xpath).select_by_visible_text(value)
            except:
                try:
                    xpath.send_keys(value)
                except:
                    pass
        tries = tries + 1
        if tries == 3:
            break
        time.sleep(2)


def checkIfElementExists(driver, xpath=None, cssSelector=None):
    try:
        if xpath:
            driver.find_element(By.XPATH, xpath)
        else:
            driver.find_element(By.CSS_SELECTOR, cssSelector)
        return True
    except NoSuchElementException:
        return False

# Wait until the page is loaded
def waitUIBlock(driver):
    driver.implicitly_wait(1)
    while len(driver.find_elements(By.XPATH, "//div[contains(@class,'blockUI')]")) > 0:
        pass
    driver.implicitly_wait(implicitWait)


# Go to new browser tab that opened recently
def switchToLatestTab(driver):
    retries = 1
    while retries < int(waitTimeout):
        if len(driver.window_handles) < 2:
            time.sleep(0.5)
            retries = retries + 1
        else:
            break
    if retries == int(waitTimeout):
        pytest.fail('Window not opened')
    driver.switch_to.window(driver.window_handles[-1])




