import ddt
import unittest
from login import login
from 封装成类_handle_excel import HandleExcel

he = HandleExcel('login_cases_data.xlsx', 'Sheet1')
datas = he.getDatas()
he.close()

print(datas)

@ddt.ddt
class TestLogin(unittest.TestCase):

    @ddt.data(*datas)
    def test_login_success(self, value):
        result = login(str(value['id']), value['pwd'])
        self.assertEqual(result, value['expect'])
        ## msg用于打印错误信息
