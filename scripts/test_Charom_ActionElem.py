from time import sleep
from selenium import webdriver


class Test_Action:
    # 使用谷歌浏览器自动化操作百度，包括点击，输入文字。。

    def test_ActionElem(self):
        driver = webdriver.Chrome()     # 创建谷歌浏览器驱动
        driver.get("https://www.baidu.com")     # 打开百度
        driver.maximize_window()     # 最大化网页窗口
        sleep(5)     # 等待5秒
        driver.find_element_by_id("kw").send_keys("12306")     # 在百度输入框输入12306
        driver.find_element_by_id("su").click()     # 点击搜索
        sleep(2)     # 等待2秒
        driver.find_element_by_link_text("官方").click()     # 点击含有官方的网站
        huoqu = driver.window_handles     # 获取浏览器窗口
        driver.switch_to.window(huoqu[1])     # 切换到第二个浏览器窗口
        sleep(2)     # 等待2秒
        driver.find_element_by_id("form-realname").send_keys("xxxxx")     # 在姓名输入框。输入xxxxx
        sleep(3)     # 等待3秒
        driver.quit()     # 清除浏览器

