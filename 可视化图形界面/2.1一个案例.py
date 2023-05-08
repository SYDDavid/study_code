## 一个实例

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QToolBar
from PySide2.QtCore import Qt

# QApplication提供了整个图形界面程序的底层管理功能，必须在任何控件被创建前，先创建它
# QMainWindow,QPushButton,QPlainTextEdit 分别为主窗体，按钮，文本框

app = QApplication([])

window = QMainWindow()  # 主窗对象window，他没有父控件，说明其为最上层对象
window.resize(500, 400)  # 主窗大小为500像素乘400像素
window.move(300, 310)  # 主窗左上角相对屏幕的坐标点位为(500,400)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")  # 设置其中默认值
textEdit.move(10, 25)  # 文本窗左上角相对主窗的坐标点为(10,25)
textEdit.resize(300, 350)  # 文本窗大小为300像素乘250像素

button = QPushButton('统计', window)
button.move(380, 80)  # 按钮窗左上角相对主窗的坐标点位为(380,80)

toolbar = QToolBar('this is toolbar')
window.addToolBar(Qt.TopToolBarArea, toolbar)

window.show()  # 使主窗口内控件全部得以展示


# app.exec_() # 结束函数

### 界面动作处理(signal，slot)

# 在Qt系统中，当界面上一个控件被操作时，就会发出一个signal。比如：被拖拽，被点击，被输入文本
# 我们可以预先捕获这些signal，并处理。处理的函数名叫slot

# 例如：

def handleClick():
    print('button被点击')


button.clicked.connect(handleClick)

app.exec_()
