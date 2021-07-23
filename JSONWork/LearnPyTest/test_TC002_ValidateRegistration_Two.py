from selenium.webdriver import Chrome



def test_registrationn_valid_data():
    path=r"D:\2\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")

def test_registrationn_invalid_data():
    path = r"D:\2\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()

def test_valid_data():
    path = r"D:\2\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")

#to test particular testcase
#pytest -k registrationn