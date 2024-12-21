import fileinput
import logging
import os
import time
from io import BytesIO
import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, SessionNotCreatedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from automationFramework.Utils.globalVariableReader import getValue, getDir
from automationFramework.Utils.locator import getLocator
from PIL import Image

# Global configuration values
waitTimeout = getValue("waitTimeout")
implicitWait = getValue("implicitWait")

@pytest.fixture()
def driver():
    """Fixture to initialize and teardown the WebDriver."""
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--unsafely-treat-insecure-origin-as-secure=http://fundfit-v3-dev.us-east-1.elasticbeanstalk.com')
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': f'{getDir()}\\Downloads\\Chrome',
        'download.prompt_for_download': False,
        'download.directory_upgrade': True
    })

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except SessionNotCreatedException:
        logging.error("Failed to create a session. Retrying...")
        driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(implicitWait)
    driver.get(getValue("ApplicationURL"))
    driver.maximize_window()
    changeReportsDir()

    yield driver

    driver.quit()

def makeScrollingScreenshot(driver):
    """Takes a full-page scrolling screenshot."""
    offset = 0
    images = []
    height = driver.execute_script("return document.documentElement.clientHeight")
    scrollBarHeight = driver.execute_script("return window.innerHeight - document.documentElement.clientHeight")
    maxHeight = driver.execute_script("return document.documentElement.scrollHeight")

    while offset < maxHeight:
        driver.execute_script(f"window.scrollTo(0, {offset});")
        time.sleep(0.2)  # Allow time for scrolling and rendering
        img = Image.open(BytesIO(driver.get_screenshot_as_png()))
        images.append(img)
        offset += height - scrollBarHeight

    imageHeight = sum([image.size[1] for image in images])
    completeImage = Image.new("RGB", (images[0].size[0], imageHeight))
    offset = 0
    for image in images:
        completeImage.paste(image, (0, offset))
        offset += image.size[1]

    return completeImage

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture screenshots on test failures."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        try:
            imageLocation = f'{getDir()}/Reports/Screenshots/Fail.png'
            os.makedirs(os.path.dirname(imageLocation), exist_ok=True)
            screenShot = makeScrollingScreenshot(item.funcargs['driver'])
            screenShot.save(imageLocation)
            with open(imageLocation, "rb") as image:
                allure.attach(
                    image.read(),
                    name='Failure Screenshot',
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            logging.error(f"Failed to capture screenshot: {e}")

def changeReportsDir():
    """Modifies the pytest configuration to update report directories."""
    cwd = os.getcwd().replace("\\", "/").split('/')
    while 'TestCases' in cwd:
        cwd.pop()
    cwd = '/'.join(cwd)

    pytest_ini_path = f'{cwd}/TestCases/pytest.ini'
    text_to_replace = 'addopts = --alluredir=../../Reports/Allure/allure-report -s --color=yes --no-header --no-summary\n'

    with fileinput.input(pytest_ini_path, inplace=True) as file:
        for line in file:
            if '../../Reports' in line:
                print(line.replace('../../Reports', f'{cwd}/Reports'), end='')
            else:
                print(line, end='')

