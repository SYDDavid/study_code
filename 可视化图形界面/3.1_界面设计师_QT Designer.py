'''
运行：
    Windows下，运行 Python安装目录下 Scripts\pyside2-designer.exe 这个可执行文件
    如果你安装的是pyqt5， 运行 Python安装目录下 X:\Python36\Lib\site-packages\qt5_applications\Qt\bin\designer.exe 可执行文件
    PyQt5工具配置：https://blog.csdn.net/weixin_40883833/article/details/126333046

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