from selenium.webdriver import Chrome
import pytest


@pytest.mark.Smoke
def test_tflex():
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


@pytest.mark.sanity
def test_validateoffice():
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


@pytest.mark.Smoke
def test_invalidoffice():
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()