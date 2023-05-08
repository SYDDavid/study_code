# 以下为一些快捷键的方式

## 代码导航                     ctrl+鼠标左键

## 快速返回                     ctrl+alt+左

## 代码对齐                     ctrl+alt+L

## 代码快速注释/取消注释          ctrl+/

## 快速查看信息                  ctrl+shift+I(光标已选中标识符)

## 快速查找哪里使用了该函数        右键-find usages

## 智能重构                     右键-refactor-rename-do refactor

### pycharm中导入模块

## 方法一：通过from import 从根目录导入

## 方法二：通过设置sources root导入

import sys

for i in sys.path:
    print(i)  # 此方法用于查询python如何查询模块文件
