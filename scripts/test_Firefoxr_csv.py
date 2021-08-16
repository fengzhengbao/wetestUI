from time import sleep
import pytest
from selenium import webdriver
from base.analyze import analyze_login_data


class Test_Csv:

    @pytest.mark.parametrize("params", analyze_login_data("login_data.json"))
    def test_csv01(self, params):
        driver = webdriver.Firefox()
        driver.get(params["browser"])
        driver.maximize_window()
        sleep(5)
        driver.quit()
