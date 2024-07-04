'''
    find_element方法，可以按照“特征”，返回一个WebElement对象。使用该对象即可实现页面操作

    库目录：            from selenium.webdriver.common.by import By

    通过特征定位的方法：
    id                  find_element(By.ID, 'username')                         ID定位，页面中ID是唯一的便于定位
    name                find_element(By.NAME, 'name')
    class               find_element(By.CLASS_NAME, 'animal')                返回第一个符合条件的WebElement对象，         若没有会报错
                        find_elements(By.CLASS_NAME, 'animal')               返回列表，内涵含所有符合条件的WebElement对象，若没有返回空列表，不会报错
                        另：<span class="chinese student">张三</span> 其中CLASS存在两个属性值 chinese和student，使用其中任一个都可定位，切勿find_element(By.CLASS_NAME, 'chinese student')
    target              find_element(By.TAG_NAME, 'span')                    可以按照当前搜索范围内的标签名称返回元素

    ***********************************************************************************************
    注：
        WebDriver提供implicitly_wait方法，可以保证全局隐式等待，后续的find_element或者find_elements都会优先等待元素出现

        WebDriver对象可以选择元素、WebElements也可以，范围不一样

    ************************************************************************************************

    注：selenium4之后，
    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_class_name('password').send_keys('sdfsdf')
    wd.find_element_by_tag_name('input').send_keys('sdfsdf')
    wd.find_element_by_css_selector('button[type=submit]').click()
    不再被支持，统一修改为：
    wd.find_element(By.ID, 'username').send_keys('byhy')
    wd.find_element(By.CLASS_NAME, 'password').send_keys('sdfsdf')
    wd.find_element(By.TAG_NAME, 'input').send_keys('sdfsdf')
    wd.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


wd = webdriver.Chrome()

# 全局隐式等待10s
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')

wd.find_element(By.TAG_NAME,)




#
# 按照上述地址获取实战获取元素
#






ready_to_quit = input('if U R ready to quit PLZ press:quit')

if ready_to_quit=='quit':

    wd.quit()