import unittest
from test_learning.unittest_自动化测试框架.login import login


class TestLogin(unittest.TestCase):

    def test_login_success(self):
        result = login('311004', 'Wan0801an!')
        self.assertEqual(result, {
            'code': 0,
            'msg': 'login success！'
        })

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
