'''
测试框架基本套路

表达用例 - 收集用例 - 执行用例 - 生成报告

TestSuite       测试套件：专门用于存储用例，抽取不同用例池中用例组成套件
    1、实例化一个TestSuite
    2、添加用例
        addTest             添加一个用例
        addTests            添加多个用例

TestLoader      用例收集：由于添加用例方式太过繁琐引入 可支持通过类名、模块名、目录方式收集
    方法一：unittest.TestLoader().discover(目录名)             通过目录搜索

'''

import unittest
from test_learning.unittest_自动化测试框架.test_login import TestLogin
from test_learning.unittest_自动化测试框架.test_register import TestRegister

s = unittest.TestSuite()

# 添加单个用例    参数为：测试类（用例名）
s.addTest(TestLogin('test_login_success'))

# 添加多个用例    参数为：[测试类（用例名）,测试类（用例名）,...]
s.addTests([TestLogin('test_login_success'), TestLogin('test_login_error')])

'''
discover(start_dir,pattern,top_level_dir)
    1、指定搜索目录
    2、文件过滤规则：test*.py
    3、用例过滤规则：测试类且继承unittest.TestCase,其中以test_开头的测试用例
'''
s1 = unittest.TestLoader().discover(r'f:\code')
print(s1)
