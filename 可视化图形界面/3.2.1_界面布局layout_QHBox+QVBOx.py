'''
按照之前的.move写法，当我们缩放窗口时，位置是固定的不会同步缩放，固引入：Layout
Layout大致分为四种：
    1、QHBoxLayout 水平布局，从左至右
    2、QVBoxLayout 垂直布局，从上至下
    3、QGridLayout 表格布局，控件可占多个格子
    4、QFormLayout 表单布局，只有两列的表格

关于QWidget、QMainWindow、QDialog:
    QmainWindow主窗口为用户提供一个应用程序框架，它有自己的布局，可以在布局中添加控件。
在主窗口中可以添加控件，比如将工具栏、菜单栏、状态栏等添加到布局管理器中。窗口类型介绍：
QMainWindow、QWidget、QDialog三个类都可以用来创建窗口，可以直接使用，也可以继承后使用。
QWidget继承于QObject和QPaintDevice，QDialog和QMainWindow则继承于QWidget，QDialog、
QMainWindow两者之间没有直接关系。QMainWindow窗口包含菜单栏、工具栏、状态栏、标题栏等，
是最常见的窗口形式，也可以说是GUI程序的主窗口。QDialog是对话框窗口的基类。对话框主要用来执
行短期任务，或者与用户进行互动，它可以是模态的，也可以是非模态的。它没有菜单栏、工具栏、状态栏等。

如果是主窗口，就使用QMainWindow类；
如果是对话框，就使用QDialog类；
如果不确定，有可能作为顶层窗口，也有可能嵌入到其他窗口，就使用QWidget类。
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
