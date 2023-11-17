# 必须基于python使用，所以一些python的库可以很好的兼容

# 1.安装
#     pip install robotframework
# 2.实践-hello world
#     编写hello.robot文件
# 3.执行
#     cmd方式：
#           指定路径下，robot <file>
###   配置插件并直接运行：
#           链接地址：https://blog.csdn.net/weixin_43487218/article/details/129204219

'''
语法规则：
    一：文本格式
        1、空格作为间隔符
        2、 | 作为间隔符
    二：文件结构
        1、Settings
    *   2、Variables             创建标量、列表、字典三种数据类型
        3、Test Cases
        4、Tasks
        5、Keywords
        6、Comments
'''

'''
    Variables三种数据类型
        标量                  ${SCALAR}
        列表                  @{LIST}
        字典                  &{DICT}
'''