from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from automationFramework.Utils.globalVariableReader import getValue


def getDriver(browser):
    if browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        service = Service(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Unsupported browser, please select 'chrome' or 'firefox'.")
    return driver


def startBrowser(url=None, browser=None):
    if not url:
        url = getValue("ApplicationURL") or "http://default-url.com"
    if not browser:
        browser = getValue("Browser") or "chrome"

    driver = getDriver(browser)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver


def stopBrowser(driver):
    driver.quit()
