from time import sleep

import pytest
from selenium import webdriver


class Test_Parameterization:
    data = [
                {"a": "https://www.baidu.com",
                 "b": "kw",
                 "c": "12306"},
                {"a": "https://www.baidu.com",
                 "b": "kw",
                 "c": "4399小游戏"}
            ]

    @pytest.mark.parametrize("params", data)
    def test_Charom_Parameterization(self, params):

        driver = webdriver.Chrome()
        driver.get(params["a"])
        driver.find_element_by_id(params["b"]).click()
        driver.find_element_by_id(params["b"]).send_keys(params["c"])
        sleep(5)
        driver.quit()