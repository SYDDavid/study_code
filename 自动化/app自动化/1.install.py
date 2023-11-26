'''
客户端(代码) - appium server(服务) - 真机/模拟器(andriod/ios)

各种语言appium
指令(Command) - 接口
请求类型、请求url、请求数据

安装appium-python客户端
pip install Appium-Python-Client


步骤：
    前置确保：1、adb连接 ip+port 2、appuim server启动
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

底层连接过程：
    1、http请求到appium server
    2、appium server通过session创建与pycharm会话
    3、获取已连接的设备列表，寻找匹配的安卓版本号
    4、是否需要安装app，参数是否配置
    5、配置工作：
        查询io.appium.settings包信息，不匹配重新安装匹配包：settings_apk-debug.apk
        appium-uiautomator2-server-v4.3.0.apk
        appium-uiautomator2-server-debug-androidTest.apk
 * 6、pycharm(port:4723) >> appium(port:8200) >> uiautomator2(port:6790)
        8200，是appium作为代理端口(proxy)，转发到设备上
        多台设备的话，需要多个代理
    7、和设备创建session会话
    8、通过4723返回给pycharm答复

adb基本命令
    adb --help

    adb kill-server
    adb start-server

    adb disconnect
    adb connect

    adb installer   + 安装包路径
    adb uninstaller + 应用包名
    adb shell dumpsys activity | find 'mFocusedActivity'        # 老版本查看 当前活跃页面
    adb shell dumpsys activity | find 'mResumedActivity'
    adb shell dumpsys activity activities | findstr mResumedActivity

    adb pull
    adb push

    adb shell

    adb logcat

    aapt dump badging + 安装包路径

    adb shell pm list packages                                  # 列出所有包名
        -f                                                      # 所有包名
        -s                                                      # 系统包
        -3                                                      # 第三方包

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
