'''
    1、创建一个.ini文件
.ini格式如下：
[section]
option:value
option:value

[section]
option:value
option:value
    2、python从ini文件读取数据
        1、引入ConfigParser类
        2、实例化
        3、调用read函数读取文件          .read('path',encoding='utf-8')
        4、调用get方法获取字符串         .get('section','option')
        4.1、调用不同方法获取内容
                                     .getboolean('section','option')
                                     .getint('section','option')
                                     .getfloat('section','option')
'''

from configparser import ConfigParser

conf = ConfigParser()
conf.read('syd_config.ini', encoding='utf-8')

value = conf.get('log', 'level')
print(value)

# 获取所有section值,return一个列表
list_section_of_conf = conf.sections()

# 获取所有section下option值
list_option_of_conf = conf.options(list_section_of_conf[0])

# 写入数据(仅做了解)
conf.set('log', 'name', 'lrs_logger')
conf.write(open('syd_config.ini', 'w', encoding='utf-8'))
