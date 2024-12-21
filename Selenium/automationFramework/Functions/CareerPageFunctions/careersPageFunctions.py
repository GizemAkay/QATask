import pytest

from automationFramework.Functions.Basic.verifyItemInPageMethod import verifyItemInPage
from automationFramework.Pages.career.CareerPage import CareerPage


@pytest.mark.xfail(raises=Exception, strict=True)
def initializeObject(driver):
    careerPageObj = CareerPage(driver)
    return careerPageObj


def openCareerPage(driver):
    careerPageObj = initializeObject(driver)
    careerPageObj.openCareersPage()
