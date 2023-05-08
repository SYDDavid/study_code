import unittest
from api_storage import api_storage
import ddt
import excel_handle

data = excel_handle.Handle_Of_Excel("api_cases.xlsx", "Register").get_data()
print(data)


@ddt.ddt
class TestRegister(unittest.TestCase):

    @ddt.data(*data)
    def test_register(self, data):
        syd = api_storage()
        result = syd.register(data['url'], data['request_data'])
        self.assertEqual(result['code'], data['expected']['code'])
        self.assertEqual(result['msg'], data['expected']['msg'])
