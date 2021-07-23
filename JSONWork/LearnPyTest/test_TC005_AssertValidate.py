from selenium.webdriver import Chrome
import pytest


#before each of testcase
#driver is local in setup method
#declaring driver in global
#yield - end of the testcase
#scope is mentioned in fixture as scope='module' only once the browser will be opened
#after completing test cases close the browser
@pytest.fixture(scope='module')
def setPath():
    global driver
    path = r"D:\2\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()

def test_registrationn_validone_data(setPath):
    driver.get("https://www.thetestingworld.com/testings/")
    assert driver.title == "1Login & Sign Up Forms"

def test_registrationn_invalidone_data(setPath):
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    assert driver.current_url == "htttps://www.thetestingworld.com/testings/"
def test_validone_data(setPath):
    driver.get("https://www.thetestingworld.com/testings/")

#to test particular grouping
#pytest -m Smoke -v
#pytest -m Sanity -v

#same way reverse - Control execution by giving tag for test case
#pytest -m "not Sanity" -v (not is keyword)