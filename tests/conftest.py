import pytest
from selenium import webdriver



@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.close()

