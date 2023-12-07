## import和import from区别
# import A 后需要A.xxx来调用A下面的函数，参数
# import A　from xxx 文件下就会拥有A下的xxx函数，可以直接通过xxx来操作

## 一些技巧
# import A,B,C 调用多个模块
# import XXX from A,B,C 调用多个标识符
# import XXX from * 模块下的全调

## 模块间命名冲突
# import A from func
# import B from func as func1

### 注意：若需要模块间共享数据最好使用列表方式传递

## 包：含有多个模块以及__init__.py文件的目录

# py3.3前，包目录里面需要有一个名字为 __init__.py 的初始化文件（一旦包被导入，其中的代码将会被执行）
# py3.3后，若包中只存放模块文件，允许不存在__init__.py，若存在同样调用下会被执行

### 注意：解释器执行过程中，最先阅读哪些包被调用。若有，执行__init__.py下内容；若无，跳过，
###      之后再按照代码顺序执行

