'''
客户端(代码) - appium server(服务) - 真机/模拟器(andriod/ios)

各种语言appium
指令(Command) - 接口
请求类型、请求url、请求数据

安装appium-python客户端
pip install Appium-Python-Client


步骤：
    1、from appium import webdriver
    2、desired_caps = {
            'automationName': 'UiAutomator2',   # 自动化框架名，需与平台匹配
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'deviceName': 'free_name',          # 设备名，必填，可任意
            'noReset':True,                     # 是否重置，True重置，False不重置
            'appPackage':'',                    # app包名，cmd获取：aapt dump badging apk路径  ### 路径不能有中文
            'appActivity':''                       # 页面名字
    }
    3、appium.remote('ip:port',desired_caps)
'''
from appium import webdriver

desired_caps = {
    'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': '127.0.0.1:16384',
    'noReset': True,
    'appPackage': 'com.hypergryph.arknights',
    'appActivity': 'com.u8.sdk.U8UnityContext'
}

webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
