'''
QGridLayout支持"栅格方式"进行快速布局
其中方法重载如下：
    1、addWidget(QWidget, r, c)                          在指定的行和列添加小部件
    2、addWidget(QWidget, r, c, rowspan, columnspan)     并指定宽度和长度
    3、addLayout(QLayout, int r, int c)                  在指定的行和列添加布局对象
'''

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

app = QApplication([])

mainwindow = QWidget()
mainwindow.resize(800, 1000)

# 创建五个按钮
button1 = QPushButton('button1')
button2 = QPushButton('button2')
button3 = QPushButton('button3')
button4 = QPushButton('button4')
button5 = QPushButton('button5')

grid = QGridLayout()
grid.addWidget(button1, 1, 1)
grid.addWidget(button2, 1, 2)
grid.addWidget(button3, 2, 1, 1, 2)
grid.addWidget(button4, 3, 1)
grid.addWidget(button5, 3, 2)

mainwindow.setLayout(grid)

mainwindow.show()
app.exec_()
