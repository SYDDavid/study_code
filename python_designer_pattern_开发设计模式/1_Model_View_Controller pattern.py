"""
模型视图控制器模式
    1、model：纯应用逻辑，通常与数据库交互，决定于向用户展示何种信息
    2、view：最终与用户交互的HTML文件，向用户展示数据
    3、controller，侦听各种信号，包括不局限于视图和查询事件
"""

import json


class Model(object):

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    @classmethod
    def getAll(self):
        database = open('db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            Model = Model(item['first_name'], item['last_name'])
            result.append(Model)
        return result

# 视图永远不会与模型交互; 控制器完成这项工作
class View():

    def showAllView(self, list):
        print('In our db we have %i users. Here they are:' % len(list))
        for item in list:
            print(item.name())

    def startView(self):
        print('MVC - the simplest example')
        print('Do you want to see everyone in my db?[y/n]')

    def endView(self):
        print('Goodbye!')

class Controller():

    def showAll(self):
        people_in_db = Model.getAll()
        return View().showAllView(people_in_db)

    def start(self):
        View().startView()
        input = input('')
        if input == 'y':
            return self.showAll()
        else:
            return View().endView()