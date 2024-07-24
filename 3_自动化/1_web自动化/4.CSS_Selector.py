'''
    CSS_Selector定位：
        1、ID                #id
        2、tag名             tag
        3、class             .class

    CSS_Selector支持“子元素”与“后代元素”定位：
        子元素：
            element1 > element2 > element3 > element4
        后代元素：
            element1   element2   element3   element4

    CSS_Selector支持属性定位：
        1、使用 [att=""]来描述            [href="http://www.miitbeian.gov.cn"]
        2、前置声明标签类型               span[href="http://www.miitbeian.gov.cn"]
        3、使用*模糊匹配                  span[href*="miitbeian"]
        4、声明属性开头^                  span[href^="http"]
        5、声明属性结尾$                  span[href$="gov.cn"]
        6、多属性匹配                     div[class=misc][ctype=gun]

    CSS_Selector的联合声明：
        可以套用上述三种方法来申明CSS选择器
            div.footer1 > span[href="http://www.miitbeian.gov.cn"]
            class为footer1的div标签下的子节点，节点标签为span，其中包含值为http://www.miitbeian.gov.cn的属性href

    CSS_Selector的组选择
        PS：个人觉得 依次搜两个列表，拼接一下是一样的效果
        1、逗号分割                              div,#BYHY                  得到div标签元素和id为BYHY的标签
        2、逗号分割与后代元素组合                 #t1 > span,p               识别：id为t1下的span和p标签
                                                #t1 > span,#t2 > p         识别：id为t1下的span标签和id为t2下的p标签
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

# 全局隐式等待10s
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

CSS_Selector = 'span'

span_list = wd.find_elements(By.CSS_SELECTOR, CSS_Selector)

for i in span_list:
    print(i.text)

ready_to_quit = input('if U R ready to quit PLZ press:quit')

if ready_to_quit == 'quit':
    wd.quit()
