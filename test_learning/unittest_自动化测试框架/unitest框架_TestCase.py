## unittest中所有用例独立执行
import unittest
from test_learning.unittest_自动化测试框架.login import login

'''
1、定义测试类，并继承unittest.TestCase 潜规则：Test开头命名表示为测试类
2、测试类中，以 test_ 开头，定义测试函数（视为测试用例）
    测试用例：
        1、测试对象
        2、测试步骤
        3、断言：预期结果与实际结果比对
        assert 逻辑表达
            TestCase自带一堆assert
            self.assertXXXXX()
        AssertionError：断言失败 - 用例直接结果Fail
'''


class TestLogin(unittest.TestCase):

    def test_login_success(self):
        result = login('311004', 'Wan0801an!')
        # assert result == {
        #     'code': 0,
        #     'msg': 'login success！'
        # }
        ## 我们采用unittest自带assert来处理
        self.assertEqual(result, {
            'code': 0,
            'msg': 'login success！'
        }, msg=None)
        ## msg用于打印错误信息

    def test_login_error(self):
        result = login('311005', 'Wan0801an!')
        assert result == {
            'code': 1,
            'msg': 'id or password Error!'
        }

    def test_login_none(self):
        result = login('', '')
        assert result == {
            'code': 2,
            'msg': 'PLZ enter id and password'
        }

'''
unittest四大核心概念
TestCase            测试用例
TestSuite           测试套件
TextTestRunner      执行结果
Fixture             前置后置

TestCase --> TestLoader --> TestSuite

'''