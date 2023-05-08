'''
在工厂模式中，创建对象时不将逻辑暴露给客户端并使用公共接口引用新创建的对象。

工厂模式使用工厂方法在Python中实现。 当用户调用方法时，我们传入一个字符串，并将返回值作为新对象通过工厂方法实现。 工厂方法中使用的对象类型由通过方法传递的字符串确定。
'''


class Button(object):
    html = ""

    def get_html(self):
        return self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class Flash(Button):
    html = "<obj></obj>"

class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()  # 将字符中第一个变大写，其余变小写
        print(globals())    # 这里会以字典类型返回当前位置的全部全局变量globals()['Image']即指向Image类
        return globals()[targetclass]()


button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).get_html())
