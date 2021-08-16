from time import sleep

from selenium import webdriver


class Test_Uics:


    def test_ui(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.maximize_window()
        sleep(5)
        driver.find_element_by_id("kw").send_keys("大鹅")
        driver.find_element_by_id("su").click()
        sleep(4)
        driver.quit()

