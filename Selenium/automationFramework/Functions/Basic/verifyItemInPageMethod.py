from automationFramework.Base.BaseClass import BaseClass


# Verify if the element is located in the page if not raise exception
def verifyItemInPage(driver, item, section):
    verifyItemInPageObj = BaseClass(driver)
    return verifyItemInPageObj.verifyItemInPage(item, section)
