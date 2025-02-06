import pytest
from selenium import webdriver



@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.close()

