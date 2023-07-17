'''
充值接口首先需要用户登录，新需求即为：
    通过别的接口返回结果作为下一个接口的传参内容
    返回过的内容需要在之后的用例执行中多次使用，但并不希望每次执行都执行登录接口重复获取id，token等信息
获取接口返回并记录后续调用，实现方式具体有以下两种：
    1、通过设置类属性，在fixture中的setupclass中定义   cls.属性，在testcase中通过 self.属性进行调用
    2、通过设置环境Env类，并结合    setattr(object,'name',value)        设置属性与对应值
                                getattr(object,'name')              获取属性对应值
                                hasattr(object,'name')              查询属性
                                delattr(object,'name')              删除属性

获取接口中具体数据：首先resp.json将返回报文转化为json格式

    安装：
        pip install jsonpath
    方式：
        jsonpath.jsonpath(对象,表达式)[]         由于jsonpath(对象,$..token)返回为匹配到的列表，故取值使用[]来按需获取想要的第几个数据

    其中$..token表示，json体中寻找所有token字段结果

    运算符：
            1、$         根目录
            2、.         子级           明确路径下搜索
            3、..        递归搜索        盲搜

# 对浮点型数据，保留n位小数，最后一位四舍五入
    round(float,n)
    "{:.nf}".format()

# 对decimal数据类型处理，通过sql语句强制转化类型
    select CAST(member.leave_amount AS CHAR) as leave_amount from ...

# 清理环境变量，重点！

    不同的测试类执行前确保env类干净
'''
import unittest
import re


# 方法二，设置全局类属性
class Env:
    pass


class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 方法二(前置)：清理环境
        dict_tmp = dict(Env.__dict__.items())
        for key, value in dict_tmp.items():
            if re.findall('__.+__', key):
                pass
            else:
                delattr(Env, key)
        # 方法一：设置为类属性，接口返回结果作为之后所有用例的入参
        cls.mum_id = 0
        cls.token = 1
        # 方法二，设置全局类属性
        setattr(Env, 'mum_id1', '0')
        # 通过jsonpath获取结果中想要的数据

    def test_recharge(self):
        print(self.mum_id)
        print(getattr(Env, 'mum_id1'))
        # print(self.token)


a = 3.1455
b = "{:.2f}".format(a)
c = round(a, 2)
print(b)
print(c)
