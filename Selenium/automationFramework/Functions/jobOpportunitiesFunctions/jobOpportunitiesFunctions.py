import pytest

from automationFramework.Pages.jobPost.jobOpportunitiesPage import JobOpportunitiesPage
from automationFramework.Utils.baseActions import selectFromDropdown
from automationFramework.Utils.locator import getLocator
from automationFramework.Utils.globalVariableReader import getValue

waitTimeout = getValue("waitTimeout")

@pytest.mark.xfail(raises=Exception, strict=True)
def initializeObject(driver):
    jobOpportunitiesObj = JobOpportunitiesPage(driver)
    return jobOpportunitiesObj

    # Filter jobs with desired options
def JobFiltering(driver, location="Istanbul, Turkey", department="Quality Assurance"):
    jobOpportunitiesObj = initializeObject(driver)
    selectFromDropdown(driver, getLocator("locationFilter","QA"), location)
    selectFromDropdown(driver, getLocator("departmentFilter","QA"), department)

