'''
需求如下：
    1、获取表头
    2、读取数据
'''

import openpyxl


class HandleExcel:

    def __init__(self, file_path, sheet_name):
        self.wb = openpyxl.load_workbook(file_path)
        self.st = self.wb[sheet_name]

    # 方法私有化，类外部将不可调用
    def _getTitle(self):
        title = []
        for items in list(self.st.rows)[0]:
            title.append(items.value)
        return title

    def getDatas(self):
        datas = []
        title = self._getTitle()
        for items in list(self.st.rows)[1:]:
            content = []
            for cell in items:
                content.append(cell.value)
            data = dict(zip(title, content))
            data[title[2]] = eval(data[title[2]])
            datas.append(data)
        return datas

    def close(self):
        self.wb.close()


if __name__ == '__main__':
    he = HandleExcel('login_cases_data.xlsx', 'Sheet1')
    datas = he.getDatas()
    print(datas)
    he.close()
