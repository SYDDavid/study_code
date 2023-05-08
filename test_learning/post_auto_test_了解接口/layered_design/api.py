'''
由于学习的接口服务器关闭，自己写了点函数来模拟接口
'''


class Api:

    def register(self, **kwargs):
        code = 0
        msg = "OK"
        '''
        :param mobile_phone:手机号
        :param pwd:密码，8-16位
        :param type:类型，0管理员，1普通用户
        :param reg_name:注册名，最长十位
        :return:
        '''
        if 'mobile_phone' not in kwargs:
            code = 1
            msg = '手机号为空'
        elif 'pwd' not in kwargs:
            code = 1
            msg = '密码为空'
        elif 'reg_name' not in kwargs:
            kwargs['reg_name'] = '小柠檬'
        elif 'type' not in kwargs:
            kwargs['type'] = 1
        elif len(kwargs['pwd']) > 16 or len(kwargs['pwd']) < 8:
            code = 2
            msg = '密码格式为8到16位'
        elif len(kwargs['mobile_phone']) != 11 or kwargs['mobile_phone'].isdigit() != True:
            code = 2
            msg = '无效的手机格式'
        elif len(kwargs['reg_name']) > 10:
            code = 2
            msg = '用户昵称长度超过10位'
        elif kwargs['type'] != 0 and kwargs['type'] != 1:
            code = 2
            msg = '不支持的用户类型'

        return {
            'code': code,
            'msg': msg
        }



if __name__ == '__main__':
    data = {'mobile_phone': '15669014429', 'pwd': 'Fire0801fly', 'type': 1}

    expect = {
        'code': 0,
        'msg': 'OK'
    }

    syd = Api().register(**data)
    print(syd)
