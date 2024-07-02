import unittest
import ddt
import os
from test_learning.post_auto_test_了解接口.layered_design.Common.handle_excel import Handle_Of_Excel
from test_learning.post_auto_test_了解接口.layered_design.Common.handle_path import TestData_path
from test_learning.post_auto_test_了解接口.layered_design.api import Api
import traceback

data = Handle_Of_Excel(os.path.join(TestData_path, "api_cases.xlsx"), "Register").get_data()


# print((data[0]['request_data'])
# print(data)

@ddt.ddt
class TestRegister(unittest.TestCase):

    @ddt.data(*data)
    def test_register(self, value):
        print(value['request_data'])
        result = Api().register(**value['request_data'])
        try:
            self.assertEqual(value['expected']['code'], result['code'])
            self.assertEqual(value['expected']['msg'], result['msg'])
        except KeyError:
            print(value['request_data'])
            print(value['expected'])
            print(result)
            raise AssertionError
