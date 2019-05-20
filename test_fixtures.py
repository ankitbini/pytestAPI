from selenium.webdriver import Chrome
import pytest


@pytest.fixture()
def setPath():
    global  driver
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()


def test_tflexfixcture(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


def test_validateofficefix(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


def test_invalidofficefixs(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()