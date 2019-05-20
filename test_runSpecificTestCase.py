from selenium.webdriver import Chrome

def test_order():
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


def test_validateoffice():
    path = "D:\\Ankit\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()