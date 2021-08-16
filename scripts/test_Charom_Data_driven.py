from time import sleep

import pytest
from selenium import webdriver

from base.analyze import analyze_login_data


class Test_Data_driven:
    # 使用json文件驱动谷歌浏览器打开百度，淘宝网页
    @pytest.mark.parametrize("pramas", analyze_login_data("login_data.json"))
    def test_csv01(self, pramas):
        driver = webdriver.Chrome()
        driver.get(pramas["browser"])
        driver.maximize_window()
        sleep(5)
        driver.quit()
