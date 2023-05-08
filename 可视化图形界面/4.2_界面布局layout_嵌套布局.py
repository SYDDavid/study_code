'''
1、设置小box
2、大layout去.addLayout(hbox1)
'''

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication([])

mainwindow = QWidget()
mainwindow.resize(800, 1000)

# 创建五个按钮
button1 = QPushButton('button1')
button2 = QPushButton('button2')
button3 = QPushButton('button3')
button4 = QPushButton('button4')
button5 = QPushButton('button5')

hbox1 = QHBoxLayout()
hbox1.addWidget(button1)
hbox1.addWidget(button2)

hbox2 = QHBoxLayout()
hbox2.addWidget(button4)
hbox2.addWidget(button5)

mainbox = QVBoxLayout()
mainbox.addLayout(hbox1)
mainbox.addWidget(button3)
mainbox.addLayout(hbox2)

# 做绑定
mainwindow.setLayout(mainbox)

mainwindow.show()
app.exec_()
