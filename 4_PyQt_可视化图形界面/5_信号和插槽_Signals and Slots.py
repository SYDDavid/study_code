'''
GUI中程序由events(事件)驱动，每个PyQt小部件都是从QObject类派生的，旨在发出“ signal ”以响应一个或多个事件。
信号本身不会执行任何操作。 相反，它“连接”到“ slot ”。插槽可以是任何callable Python function。

PyQt中有两种实现方式，实现signal与slots的连接
    方式一：QtCore.QObject.connect(widget, QtCore.SIGNAL(‘signalname’), slot_function)
    方式二：widget.signal.connect(slot_function)
'''

from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


class mainwin:

    def __init__(self):
        self.window = QWidget()

        self.button1 = QPushButton('button1', self.window)
        self.button2 = QPushButton('button2', self.window)
        self.button3 = QPushButton('button3', self.window)
        self.button4 = QPushButton('button4', self.window)

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.button1)
        self.mainlayout.addWidget(self.button2)
        self.mainlayout.addWidget(self.button3)
        self.mainlayout.addWidget(self.button4)

        self.window.setLayout(self.mainlayout)

        self.button1.clicked.connect(self.button1_click)

        # 信号与信号的关联
        self.button2.clicked.connect(self.button3.clicked)
        self.button3.clicked.connect(self.button3_click)

        # 解除关联，缺省为解除所有关联
        self.button4.clicked.connect(self.button4_click)
        self.button4.clicked.disconnect(self.button4_click)

    def button1_click(self):
        print('this is button1')

    def button3_click(self):
        print('this is button3')

    def button4_click(self):
        print('this is button4')


if __name__ == '__main__':
    app = QApplication([])
    syd = mainwin()
    syd.window.show()
    app.exec_()
