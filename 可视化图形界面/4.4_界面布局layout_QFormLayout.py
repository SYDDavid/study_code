'''
QFormLayout支持"表单方式"进行快速布局
内置方法如下：
    1、addRow(QLabel, QWidget)               添加标签、小组件的行
    2、addRow(QLabel, QLayout)               添加标签、子布局的行
    3、addRow(QWidget)                       添加整行的小组件
'''

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QRadioButton, QHBoxLayout, \
    QPushButton, QFormLayout

app = QApplication([])

window = QWidget()
window.resize(80, 100)

mainlayout = QFormLayout()

# 设计首行
lab1 = QLabel('Name')
mainlayout.addRow(lab1, QLineEdit())

# 设计第二行
lab2 = QLabel('Address')
vbox = QVBoxLayout()
vbox.addWidget(QLineEdit())
vbox.addWidget(QLineEdit())
mainlayout.addRow(lab2, vbox)

# 设计第三行
lab3 = QLabel('sex')
hbox = QHBoxLayout()
r1 = QRadioButton("Male")
r2 = QRadioButton("Female")
hbox.addWidget(r1)
hbox.addWidget(r2)
# 实现左对齐
hbox.addStretch()
mainlayout.addRow(lab3, hbox)

# 设计第四行
mainlayout.addRow(QPushButton('submit'),QPushButton('cancel'))

# 设计第五行
mainlayout.addRow(QLabel("product by treehole"))

window.setLayout(mainlayout)

window.show()
app.exec_()
