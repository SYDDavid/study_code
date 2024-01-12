from PyQt5.QtWidgets import *


class View():

    def __init__(self):

        self.app = QApplication([])
        self.window = QWidget()
        self.window.resize(300, 200)

        self.name = QLineEdit('', self.window)
        self.pwd = QLineEdit('', self.window)
        self.button = QPushButton('run', self.window)

        # layout竖直排列, 通过addStretch（）方法在它们之间添加可伸展的空白空间。
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.name)
        mainlayout.addWidget(self.pwd)
        mainlayout.addWidget(self.button)
        self.window.setLayout(mainlayout)

        # self.window.show()

    def get_name(self):
        return self.name.text()

    def get_pwd(self):
        return self.pwd.text()

    def window_show(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    v = View()
    v.window_show()