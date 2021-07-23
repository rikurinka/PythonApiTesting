#method need to be created for testcase
#method name should start with test
from selenium.webdriver import Chrome
import pytest

a= 100

@pytest.mark.skipif(a>100,reason="Dont want to execute on current build")
def test_registration_onevalid_data():
    path = "D:\\2\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings")


@pytest.mark.skip("Dont want to execute on current build")
def test_registration_valid_data():
    path = "D:\\2\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings")

#Note: If u want to execute pytest in cmd propmt
#goto file location -> type -> pytest and click enter
#terminal -> type ->pytest
def test_registration_invalid_data():
    path = "D:\\2\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings")
    driver.maximize_window()

#to check which testcase name is skipped in pytest

#commandprompt-> pytest -v

#-v is verbose which display the detailed test case report

