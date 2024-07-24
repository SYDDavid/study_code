'''
    对元素进行操控大致分为三大类：
        1、点击                       click                点击位置为：目标元素中心点
        2、输入字符串                 clear                 清空字符串元素内容
                                     send_keys             输入新字符串
        3、获取信息                   text                  获取元素内文字内容
                                    get_attribute('')       获取元素内某属性的值
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

# 全局隐式等待10s
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')





# 清空与输入字符串
kw = wd.find_element(By.ID, 'kw')
kw.clear()
kw.send_keys('123')

# 点击动作
suggestion = wd.find_element(By.ID, 'suggestion')
suggestion.click()

# 获取信息
foot = wd.find_element(By.ID, 'go')
print(foot.text)
print(foot.get_attribute('style'))





ready_to_quit = input('if U R ready to quit PLZ press:quit')

if ready_to_quit == 'quit':
    wd.quit()
