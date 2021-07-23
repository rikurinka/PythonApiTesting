from selenium.webdriver import Chrome
import pytest

@pytest.mark.Smoke
def test_registrationn_valid_data():
    path=r"D:\2\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")

@pytest.mark.Sanity
def test_registrationn_invalid_data():
    path = r"D:\2\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
@pytest.mark.Smoke
def test_valid_data():
    path = r"D:\2\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")

#to test particular grouping
#pytest -m Smoke -v
#pytest -m Sanity -v

#same way reverse - Control execution by giving tag for test case
#pytest -m "not Sanity" -v (not is keyword)