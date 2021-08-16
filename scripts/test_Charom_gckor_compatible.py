from time import sleep

from selenium import webdriver

class Test_Compatible:

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

