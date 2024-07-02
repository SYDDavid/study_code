'''
    中文文档地址：https://www.osgeo.cn/requests/index.html

接口四大部分
    1、接口地址
    2、请求方法
    3、请求参数
    4、响应数据

get：param
    没有请求体
    param是追加在url后的查询参数
    url?key=value&key=value&key=value
post：data，json
    有两种不同请求体
    data:字典，格式为application/x-www-form-urlencoded
    json:字典，格式为application/json
    
'''

import requests

# requests.get()
url = 'http://api.lemonban.com/futureloan/member/register'
data = {'mobile_phone': '15669014428', 'pwd': 'Wan0801an'}
headers = {'X-Lemonban-Media-Type': 'lemonban.v2'}
resp = requests.post(url, json=data, headers=headers)
# 响应状态码
# print(resp.status_code)
# print('*' * 50)

# 响应头
# print(resp.headers)
# print('*' * 50)

# 响应体
print(resp.text)
print('*' * 50)

# 响应体为网络传输中的内容，故为str类型
# requests函数提供json方法转化为dict对象
## 注意：不使用eval方法因为，响应体内部存在null的情况可能导致无法完成转换
# print(resp.json())
# print(type(resp.json()))
# print('*' * 50)
