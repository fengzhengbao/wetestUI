from time import sleep


from selenium import webdriver


class Test_Jietu:

    # 使用火狐浏览器截图保存
    def test_Variable01(self):
        aa = "aa.png"
        driver = webdriver.Firefox()
        driver.get("https://www.baidu.com")
        driver.maximize_window()
        sleep(5)
        driver.save_screenshot(aa)
        driver.quit()


