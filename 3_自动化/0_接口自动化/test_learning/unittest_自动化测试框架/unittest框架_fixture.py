'''
测试用例：
    1、测试对象
    2、测试步骤
    3、断言：预期结果与实际结果比对
    assert 逻辑表达
        TestCase自带一堆assert
        self.assertXXXXX()
    AssertionError：断言失败 - 用例直接结果Fail
    4、前置后置工作 - fixture
        setUp               在测试类中每一个用例执行前都会执行一遍setUp
        tearDown            在测试类中每一个用例执行后都会执行一遍tearDown
        setUpClass          在测试类中第一个用例执行前执行一遍setUp
        tearDownClass       在测试类中最后一个用例执行后执行一遍tearDown

    ###注意：setUpClass 和 tearDownClass前要加语法糖 @classmethod
'''

import unittest
from test_learning.unittest_自动化测试框架.login import login

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('*********登录类测试开始执行*********')

    @classmethod
    def tearDownClass(cls):
        print('*********登录类测试执行结束*********')


    def setUp(self) -> None:
        print('=========单个用例开始执行=========')

    def tearDown(self) -> None:
        print('=========单个用例执行结束=========')


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