"""
测试过程中会遇到json与dict中空表达不一致，具体表现为：
    json：null
    dict：None
"""
import json

ss_json = '{"mobile_phone":"18600001112","pwd":"123456789","type":1,"reg_name":"美丽可爱的小简","flag":null}'

# json字符串转换成字典
ss_dict = json.loads(ss_json)
print(ss_dict)

dict_ss = {'mobile_phone': '18600001112', 'pwd': '123456789', 'type': 1, 'reg_name': '美丽可爱的小简', 'flag': None}
# 将字典转换成json字符串
ss_json = json.dumps(dict_ss, ensure_ascii=False)
print(ss_json)
