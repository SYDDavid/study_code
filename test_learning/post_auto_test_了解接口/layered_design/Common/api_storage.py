import requests


# 创建接口库，包含所有接口功能
class api_storage:

    def __init__(self):
        self.headers = {'X-Lemonban-Media-Type': 'lemonban.v2'}

    def register(self, url, json):
        resp = requests.post(url, json=json, headers=self.headers)
        return resp.text

    def login(self, url, json):
        resp = requests.post(url, json=json, headers=self.headers)
        resp_dict = resp.json()
        token = resp_dict['data']['token_info']['token']
        self.headers['Bearer token_value'] = token
        return resp.text


# 验证下通过登录，headers可以获到token
if __name__ == '__main__':
    syd = api_storage()
    print(syd.headers)
    res = syd.register('http://api.lemonban.com/futureloan/member/register',
                       {"mobile_phone": "15669014430", "pwd": "Fire0801fly", "type": 1, "reg_name": "firefly"})
    print(res)
