'''
按照之前的.move写法，当我们缩放窗口时，位置是固定的不会同步缩放，固引入：Layout
Layout大致分为四种：
    1、QHBoxLayout 水平布局，从左至右
    2、QVBoxLayout 垂直布局，从上至下
    3、QGridLayout 表格布局，控件可占多个格子
    4、QFormLayout 表单布局，只有两列的表格

步骤：
    1、导包                from PyQt5.QtWidgets import QVBoxLayout,Qwidget
    2、实例化顶层窗口        QWidget()
    3、实例化组件           QVBoxLayout()
    4、按序添加排列         addWidget()            添加组件
                         addStretch()          添加空白空间
    5、绑定布局与窗口       window.setLayout(mainlayout)
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

app = QApplication([])
window = QWidget()
window.resize(400, 600)

# 创建四个点击按钮
button1 = QPushButton('button1', window)
button2 = QPushButton('button2', window)
button3 = QPushButton('button3', window)
button4 = QPushButton('button4', window)

# layout竖直排列, 通过addStretch（）方法在它们之间添加可伸展的空白空间。
mainlayout = QVBoxLayout()
mainlayout.addWidget(button1)
mainlayout.addStretch()
mainlayout.addWidget(button2)
# mainlayout.addStretch()
mainlayout.addWidget(button3)
# mainlayout.addStretch()
mainlayout.addWidget(button4)

window.setLayout(mainlayout)

window.show()
app.exec_()
