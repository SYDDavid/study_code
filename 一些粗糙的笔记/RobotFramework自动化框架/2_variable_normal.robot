*** Settings ***
Documentation    Suite description

*** Test Cases ***
Buildin Normal Variable
    [Tags]    常用内置变量
    LOG    当前测试用例文件的绝对路径为：${CURDIR}
    LOG    临时目录的绝对路径为：${TEMPDIR}
    LOG    执行用例的绝对路径为：${EXECDIR}
    LOG    当前系统目录分隔符：${/}
    LOG    当前系统多路径分隔符：${:}
    LOG    当前系统换行符：${\n}