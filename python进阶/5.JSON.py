import json

# 序列化与反序列化

# 序列化是为了解决不同语言程序在网络传输过程中间对象格式的差异性

## xml/json

# xml的弊端在于序列化性能相对较低，而且转化后的数据体积增大
# json是目前主流且轻量化的数据交换格式

### 实例：
# 首先：创建一个实例对象

historyTransactions = [

    {
        'time': '20170101070311',  # 交易时间
        'amount': '3088',  # 交易金额
        'productid': '45454455555',  # 货号
        'productname': 'iphone7'  # 货名
    },
    {
        'time': '20170101050311',  # 交易时间
        'amount': '18',  # 交易金额
        'productid': '453455772955',  # 货号
        'productname': '奥妙洗衣液'  # 货名
    }

]

jsonstr = json.dumps(historyTransactions)  # dumps意为倾倒
print(jsonstr)

print('*' * 50)

## 注意：json格式本身就是个字符串

print(json.dumps(historyTransactions, ensure_ascii=False,
                 indent=4))  # ensure_ascii=False 表示遇到非ascii码(中文)就会按照原来的表示，indent表示前缩进4

# 反序列化

content = json.loads(jsonstr)
print(content)
print(type(content))