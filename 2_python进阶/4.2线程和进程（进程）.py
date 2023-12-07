### 当我们需要调用计算机多核性能时就需要用到多进程操作

from multiprocessing import Process, Manager
from time import sleep


def f():
    while True:
        b = 53 * 53


if __name__ == '__main__':
    plist = []
    for i in range(2):
        p = Process(target=f)  # 和线程的调用如出一辙
        p.start()
        plist.append(p)

    for p in plist:
        p.join()


# 获取子进程中的计算结果 multiprocessing.Manager

def f(taskno, return_dict):
    sleep(2)
    # 存放计算结果到共享对象中
    return_dict[str(taskno)] = '你想读取的数据'


if __name__ == '__main__':
    manager = Manager()
    # 创建 类似字典的 跨进程 共享对象
    return_dict = manager.dict()
    plist = []
    for i in range(10):
        p = Process(target=f, args=(i, return_dict))
        p.start()
        plist.append(p)

    for p in plist:
        p.join()

    print('get result...')
    # 从共享对象中取出其他进程的计算结果
    for k, v in return_dict.items():
        print(k, v)
