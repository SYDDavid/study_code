'''
安卓系统
    原生控件+html

原生控件的定位：第三方工具
    uiautmatorviewer:
        1、设备不能被占用
        2、adb devices要识别到设备

    text:               页面内如果文本唯一，可定位
    resourced-id:       组件一致可能导致不唯一，不可定位
    content-desc:       不一定每一个app有，盲人使用，可定位

css：定位方式？？
xml：xpath定位

若id唯一会显示提供

工具：uiAutomator2
    步骤：
        1、安装：               pip install -U uiAutomator
        2、安装定位工具          pip install -U weditor
        3、启动weditor         cmd进入weditor

'''