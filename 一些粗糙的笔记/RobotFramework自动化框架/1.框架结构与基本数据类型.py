# 必须基于python使用，所以一些python的库可以很好的兼容

# 1.安装
#     pip install robotframework
# 2.实践-hello world
#     编写hello.robot文件
# 3.执行
#     cmd方式：
# #         指定路径下，robot <file>
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
        
标量赋值：
    一、在Variables文件中使用
        1、${变量名}    值
    二、在Testcases用例中使用
        1、set赋值法
            ${boyname}  Set Variable    Tom
            ${girlname} Set Variable  if  2==3    Alice   Lucky
            增加逻辑判断若满足条件赋值A，若不满足赋值B
        2、支持切片获取数据
            log     first_name：${boyname}[0]
            
列表赋值：
    一、在Variables文件中使用
        1、@{变量名}    值1  值2  值3
    二、在Testcases用例中使用
        1、set赋值法
            @{boysname}     Set Variable    Tom    Judy    Moly
        2、Collections库create
            ${girlsname}     create list    Julia    Alice   Lucky
    三、Collections库中一些关键字                                             注意：必须导入Collections！！！
            append to list  ${list_name}    value                       插入末尾
            insert into list  ${list_name}    index     value           把value插入index位置，与python中list计数规则一致
            
            remove from list    ${list_name}    index                   取出索引下的数据
            remove values from list     ${list_name}    value           取出value

字典赋值：
    一、在Variables文件中使用
        1、&{变量名}    key1=value1     key2=value2     key3=value3     key4=value4
    二、在Testcases用例中使用（无set variable方法）
        1、Collections库中的create
            ${用户1}      create dictionary   用户名=张三   地址=深圳
    三、Collections库中一些关键字
            set to dictionary   ${dict}     key4=value4     key5=value5         插入数据
            remove from dictionary      ${dict}     key                         字典里删除某key
            ${value}   pop from dictionary    ${dict}     key                   字典里取出某key的value
            keep in dictionary      ${dict}     key                             只保留某key，删除其他key
'''