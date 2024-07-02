'''
布局可以设置对齐方式
对齐类Align...在PyQt5.QtCore.Qt中

常用的有：
    1、AlignCenter: 居中
    2、AlignLeft: 居左
    3、AlignRight: 居右
    4、AlignTop: 居顶
    5、AlignBottom: 居底

语法格式如下：
    layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)         # 布局内组件左上放置
'''

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

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
mainlayout.addWidget(button2)
mainlayout.addWidget(button3)
mainlayout.addWidget(button4)

# 左上对齐放置
mainlayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

window.setLayout(mainlayout)

window.show()
app.exec_()
