'''
五种元素定位方式：
    1、id
    2、xpath
    3、class_name
    通过By方式定位操作

    4、android_uiautomator   (UiAutomator2)  文本定位
    5、accessibility_id      (description)
    通过MobileBy定位操作

    6、坐标

android_uiautomator框架      java语言-字符串必须是双引号

    new UiSelector().resourceId("")  # appium 1.15之前
    resourceId("")   # appium 1.15之后

属性组合
resourceId("").text("")
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

# 引入等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

desired_caps = {
    'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': '127.0.0.1:16384',
    'noReset': True,
    'appPackage': 'com.hypergryph.arknights',
    'appActivity': 'com.u8.sdk.U8UnityContext'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# driver启动需要等待
loc = (MobileBy.ID, 'com.mumu.launcher:id/preview_background')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))

# appium方式
driver.find_element(MobileBy.ID, 'com.mumu.launcher:id/preview_background').click()

# UiSelector方式
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.mumu.launcher:id/preview_background")')
# 注意函数名表达，使用双引号
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
