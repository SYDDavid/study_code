'''
.yaml文件一种数据表达，即：可以直接转换为py对象，整个文件将转换为字典或者列表

基本规则：
    1、大小写敏感
    2、使用缩进表示层级关系
    3、禁止使用tab缩进，必须使用空格
    4、缩进长度没有限制，元素处于同一长度即为同一层级

书写格式：文件内只能全为字典或者全为列表
    字典格式：以冒号：作为间隔且冒号后存在空格
    列表格式：以减号-作为间隔且减号后存在空格

python读取yaml数据
    1、引入pyyaml       import yaml
    2、打开yaml文件      open('path',encoding='utf-8')
    3、调用load函数      yaml.load(fs,yaml.FullLoader)
'''

import yaml

# fs = open('syd_config_dict.yaml', encoding='utf-8')
# dic = yaml.load(fs, yaml.FullLoader)

with open('syd_config_dict.yaml', encoding='utf-8') as fs:
    dic = yaml.load(fs, yaml.FullLoader)
print(dic)
