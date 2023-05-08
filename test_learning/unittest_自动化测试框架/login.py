def login(id, pwd):
    if id != '' and pwd != '':
        if id == '311004' and pwd == 'Wan0801an!':
            return {
                'code': 0,
                'msg': 'login success！'
            }
        else:
            return {
                'code': 1,
                'msg': 'id or password Error!'
            }
    else:
        return {
            'code': 2,
            'msg': 'PLZ enter id and password'
        }
