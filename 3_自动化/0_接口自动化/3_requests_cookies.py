'''
requests自带session类：对应为一次会话对象
好处为，使用会话对象登陆后，自动会记录cookies，以便后续使用

使用：
        1、创建session对象
        2、登录使对象自动获取到cookies
        3、使用其他url
'''

import requests

s = requests.Session()

print('登录前cookies：', s.cookies)

url = 'https://www.ketangpai.com/UserApi/login'
data = {'email': '2522337205@qq.com',
        'password': 'nmb_python',
        'member': 0}
s.post(url, data=data)

print('登录后cookies:', s.cookies)

url_get_info = 'https://www.ketangpai.com/UserApi/getUserInfo'
resp = s.get(url_get_info)
print(resp.text)
