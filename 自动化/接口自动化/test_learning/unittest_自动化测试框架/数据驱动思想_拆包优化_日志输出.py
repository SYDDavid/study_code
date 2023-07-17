'''
定义函数传参确定后，通过元组传参，若个数一致可通过拆包实现
'''

import ddt
import unittest
from login import login
from test_learning.logger_日志模块.logging_become_class import my_logger

datas = [
    {'param': ('311004', 'Wan0801an!'), 'expect': {
        'code': 0,
        'msg': 'login success！'
    }},
    {'param': ('311005', 'Wan0801an!'), 'expect': {
        'code': 1,
        'msg': 'id or password Error!'
    }},
    {'param': ('', ''), 'expect': {
        'code': 2,
        'msg': 'PLZ enter id and password'
    }},
]


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        my_logger.info('*' * 10 + '用例开始执行' + '*' * 10)

    def tearDown(self) -> None:
        my_logger.info('*' * 10 + '用例执行结束' + '*' * 10)

    @ddt.data(*datas)
    def test_login_success(self, value):
        result = login(*value['param'])
        my_logger.info('入参为：{}'.format(value))
        self.assertEqual(result, value['expect'])
        my_logger.info('结果为：{}'.format(result))
        # msg用于打印错误信息
