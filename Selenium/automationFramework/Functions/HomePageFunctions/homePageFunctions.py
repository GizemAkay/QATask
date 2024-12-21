import pytest

from automationFramework.Pages.home.homePage import HomePage
from automationFramework.Utils.baseActions import waitUIBlock
from automationFramework.Utils.globalVariableReader import getValue

waitTimeout = getValue("waitTimeout")
implicitWait = getValue("implicitWait")


@pytest.mark.xfail(raises=Exception, strict=True)
def initializeObject(driver):
    return HomePage(driver)


def verifyHomePage(driver):
    homePageObj = initializeObject(driver)
    assert homePageObj.verifyHomePageOpened()


def handleCookies(driver):
    homePageObj = initializeObject(driver)
    homePageObj.handleCookies()
