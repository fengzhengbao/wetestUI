from time import sleep
from selenium import webdriver


class Test_Action:
    # 使用谷歌浏览器自动化操作百度，包括点击，输入文字。。

    def test_ActionElem(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.maximize_window()
        sleep(5)
        driver.find_element_by_id("kw").send_keys("12306")
        driver.find_element_by_id("su").click()
        sleep(2)
        driver.find_element_by_link_text("官方").click()
        huoqu = driver.window_handles
        driver.switch_to.window(huoqu[1])
        sleep(2)
        driver.find_element_by_id("form-realname").send_keys("xxxxx")
        sleep(3)
        driver.quit()

