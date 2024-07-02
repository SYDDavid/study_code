'''
token以最新登录的一次为准，重新登录会导致老的token失效

使用：
    1、手动登录获取到token
    2、添加到头部中
    3、带着新头部进行访问
'''

import requests

url_login = 'http://api.lemonban.com/futureloan/member/login'
data = {'mobile_phone': '15669014428', 'pwd': 'Wan0801an'}
headers = {'X-Lemonban-Media-Type': 'lemonban.v2'}

resp = requests.post(url_login, json=data, headers=headers)
resp_dict = resp.json()
print(resp_dict)
id = resp_dict['data']['id']
token = resp_dict['data']['token_info']['token']

url_recharge = 'http://api.lemonban.com/futureloan/member/recharge'
headers['Authorization'] = 'Bearer ' + format(token)
data_recharge = {'member_id': id, 'amount': 2000}

resp = requests.post(url_recharge, json=data_recharge, headers=headers)
print(resp.json())
