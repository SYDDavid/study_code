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

        1、逗号分割                              div,#BYHY                  得到div标签元素和id为BYHY的标签
        2、逗号分割与后代元素组合                 #t1 > span,p               识别：id为t1下的span + 全页面的p标签
                                                #t1 > span,#t1 > p         识别：id为t1下的span标签和 + id为t1下的p标签

        注意：组选择下的返回，按照子组合定位元素，依次定位后，按照原html出现顺序依次展示！！
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

# 全局隐式等待10s
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

CSS_Selector = '#t1 > span , #t1 > p'

element_list = wd.find_elements(By.CSS_SELECTOR, CSS_Selector)

for element in element_list:
    print(element.text)

# 组选择下按照原html展示顺序验证

print('*'*50)

CSS_Selector2 = '#t2 > span , #t1 > span , #t1 > p'

element_list = wd.find_elements(By.CSS_SELECTOR, CSS_Selector2)

for element in element_list:
    print(element.text)

ready_to_quit = input('if U R ready to quit PLZ press:quit')

if ready_to_quit == 'quit':
    wd.quit()
