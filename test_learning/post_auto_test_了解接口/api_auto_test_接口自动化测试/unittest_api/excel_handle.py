'''
该模块功能如下：
    输入：文件名与表单名
    输出：列表其中每个元素为一个字典
         字典内容为：标题：内容
         若其中字符串内容为字典格式，自动转化为字典格式
'''

import openpyxl


class Handle_Of_Excel:

    def __init__(self, path, sheet_name):
        self.wb = openpyxl.load_workbook(path)
        self.st = self.wb[sheet_name]

        title = []
        for items in list(self.st.rows)[0]:
            title.append(items.value)

        self.title = title

    def _get_data_row(self, num_rows):
        data_rows = []
        for items in list(self.st.rows)[num_rows]:
            data_rows.append(items.value)
        data_rows = self._deal_dict_content(data_rows)
        dict_row = dict(zip(self.title, data_rows))

        return dict_row

    def get_data(self, num_rows=0):
        data_list = []
        if num_rows:
            dict_row = self._get_data_row(num_rows)
            data_list.append(dict_row)
        else:
            length_row = self.st.max_row
            for i in range(length_row - 1):
                dict_row = self._get_data_row(i + 1)
                data_list.append(dict_row)
        return data_list

    # 循环遍历元素，若可转化为字典，则转换
    def _deal_dict_content(self, list):
        res_list = []
        for item in list:
            if (item[0] == '{') & (item[-1] == '}'):
                res_list.append(eval(item))
            else:
                res_list.append(item)
        return res_list


if __name__ == '__main__':
    path = 'api_cases.xlsx'
    syd = Handle_Of_Excel(path, 'Register')
    print(syd.get_data())
