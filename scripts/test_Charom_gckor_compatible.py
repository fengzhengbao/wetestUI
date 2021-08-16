from time import sleep

from selenium import webdriver

class Test_Compatible:

    # 兼容测试，使用谷歌，火狐打开百度网页
    def test_compatible01(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.maximize_window()
        sleep(2)
        driver.quit()
    def test_compatible02(self):
        driver = webdriver.Firefox()
        driver.get("https://www.baidu.com")
        driver.maximize_window()
        sleep(2)
        driver.quit()

