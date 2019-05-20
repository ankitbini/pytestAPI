from selenium.webdriver import Chrome
import pytest

'''If we define scope = module then it means the fixture run only once.
   in the below example browser open only once, all the three test case are execute in that single browser and after all
   execution the browser will close'''
@pytest.fixture(scope="module")
def setPath():
    global  driver
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()


def test_fixcture(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()
    print(driver.title)

def test_officefix(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()
    print(driver.current_url)
    assert driver.current_url == "abcd"


def test_officefixs(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()