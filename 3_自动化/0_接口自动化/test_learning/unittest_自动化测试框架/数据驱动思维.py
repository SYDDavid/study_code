'''
设计思维：ddt            data driven test
同一流程，入参不同，预期结果不同，形成n组用例

py对应模块：ddt
    1、在测试类名上，@ddt.ddt
    2、在测试用例上，@ddt.data(*列表) *列表拆包
    3、在测试用例中，设置参数用于接收拆包后数据
'''

import ddt
import unittest
from login import login

# 将多组测试数据，依次传递给同一流程


# class TestLogin(unittest.TestCase):
#
#     def test_login_success(self):
#         result = login('311004', 'Wan0801an!')
#         # assert result == {
#         #     'code': 0,
#         #     'msg': 'login success！'
#         # }
#         ## 我们采用unittest自带assert来处理
#         self.assertEqual(result, {
#             'code': 0,
#             'msg': 'login success！'
#         }, msg=None)
#         ## msg用于打印错误信息
#
#     def test_login_error(self):
#         result = login('311005', 'Wan0801an!')
#         assert result == {
#             'code': 1,
#             'msg': 'id or password Error!'
#         }
#
#     def test_login_none(self):
#         result = login('', '')
#         assert result == {
#             'code': 2,
#             'msg': 'PLZ enter id and password'
#         }


datas = [
    {'id': '311004', 'pwd': 'Wan0801an!', 'expect': {
        'code': 0,
        'msg': 'login success！'
    }},
    {'id': '311005', 'pwd': 'Wan0801an!', 'expect': {
        'code': 1,
        'msg': 'id or password Error!'
    }},
    {'id': '', 'pwd': '', 'expect': {
        'code': 2,
        'msg': 'PLZ enter id and password'
    }},
]

@ddt.ddt
class TestLogin(unittest.TestCase):

    @ddt.data(*datas)
    def test_login_success(self, value):
        result = login(value['id'], value['pwd'])
        self.assertEqual(result, value['expect'])
        ## msg用于打印错误信息
