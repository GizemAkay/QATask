from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from automationFramework.Functions.Basic.verifyItemInPageMethod import verifyItemInPage
from automationFramework.Functions.CareerPageFunctions.careersPageFunctions import openCareerPage
from automationFramework.Functions.HomePageFunctions.homePageFunctions import verifyHomePage, handleCookies
from automationFramework.Functions.jobOpportunitiesFunctions.jobOpportunitiesFunctions import JobFiltering
from automationFramework.Utils.baseActions import waitUIBlock, ifElementClickable, switchToLatestTab
from automationFramework.Utils.globalVariableReader import getValue
from automationFramework.Utils.locator import getLocator
from selenium.webdriver.support import expected_conditions as EC


def test_main(driver):
    careerPageBlocks= [{"item": "locations", "section": "Careers", "text": "Our Locations"}, {"item": "lifeAtInsider", "section": "Careers", "text": "Life at Insider"},
                            {"item": "team", "section": "Careers", "text": "Find your calling"}]
    waitTimeout = getValue("waitTimeout")

    # Go to Homepage and verify
    verifyHomePage(driver)

    # Handle cookies if exists
    handleCookies(driver)

    # Navigate to Career Page
    openCareerPage(driver)

    # Check items in the page
    for block in careerPageBlocks:
        item = block["item"]
        section = block["section"]
        text = block["text"]
        assert text in verifyItemInPage(driver, item, section)

    # Navigate a new URL
    driver.get(getValue("qaURL"))

    # Click See All QA Jobs button
    driver.find_element(By.XPATH, getLocator("seeJobs", "QA")).click()

    # Filtering jobs according to department and location
    JobFiltering(driver)
    waitUIBlock(driver)

    # Catch main job list and check its children
    qaJobList= driver.find_element(By.XPATH, getLocator("qaJobList", "QA"))
    qaJobs = (qaJobList.find_elements(By.XPATH, "./div"))

    # check all job posts
    for job in qaJobs:
        data_team = job.get_attribute("data-team")
        data_location = job.get_attribute("data-location")

        # To verify if they have expected department and location value
        assert data_team == "qualityassurance", f"data-team mismatch: {data_team}"
        assert data_location == "istanbul-turkey", f"data-location mismatch: {data_location}"

    # Find the parent before hover action
    parent_element = WebDriverWait(driver, waitTimeout).until(EC.presence_of_element_located((By.CLASS_NAME, "position-list-item-wrapper")))

    # Perform a hover action
    actions = ActionChains(driver)
    actions.move_to_element(parent_element).perform()
    link_elements = driver.find_elements(By.XPATH, "//a[text()='View Role']")

    # Click the first visible element
    driver.find_element(By.XPATH, getLocator("viewRole","QA")).click()

    # Switch to the new browser tab
    switchToLatestTab(driver)
    waitUIBlock(driver)

    # Catch the URL and verify
    currentURL = driver.current_url
    assert "jobs.lever.co" in currentURL
