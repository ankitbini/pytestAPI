from selenium.webdriver import Chrome
import pytest

a = 1001


@pytest.mark.skipif(a > 100, reason="Don't want to run at this time")
def test_validateregistrartion():
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


def test_validate_account():
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()