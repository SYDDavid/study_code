'''
    Selenium 是一套 Web网站 自动化操作程序的解决方案，可以模拟浏览器操作
    自动化程序 --> 调用浏览器驱动 --> 操作浏览器

    1、安装 selenium库
        pip install selenium
    2、安装chrome和chrome浏览器驱动，版本需一致，chrome driver添加到path下
        https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
'''

## 下面是个简单的示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 实例化WebDriver对象，指明使用Chrome驱动
wd = webdriver.Chrome()
# 调用WebDriver的get方法，打开具体页面
wd.get('https://www.baidu.com')



ready_to_quit = input('if U R ready to quit PLZ press:quit')

if ready_to_quit=='quit':
    # 退出关闭WebDriver示例
    wd.quit()