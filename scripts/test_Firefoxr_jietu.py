from time import sleep


from selenium import webdriver


class Test_Jietu:

    def test_Variable01(self):
        aa = "aa.png"
        driver = webdriver.Firefox()
        driver.get("https://www.baidu.com")
        driver.maximize_window()
        sleep(5)
        driver.save_screenshot(aa)
        driver.quit()

