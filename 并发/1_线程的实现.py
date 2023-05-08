'''
内置库 threading
    自带函数：
        threading.activeCount()         此方法返回活动的线程对象的数量。
        threading.currentThread()       此方法返回调用者线程控件中的线程对象数。
        threading.enumerate()           此方法返回当前活动的所有线程对象的列表。
    Tread类，自带方法：
        run()                           线程的入口点。
        start()                         通过调用run方法启动一个线程。
        join([time])                    主程序必须等待线程终止。可以设置一个主程序最长等待时间
        isAlive()                       检查线程是否仍在执行。
        getName()                       返回线程的名称。
        setName()                       设置线程的名称。

有五种线程状态：新的，可运行的，运行的，等待的，死亡的。

Barrier：
    传入参数你，当n个线程加入前，所有线程处于等待状态
'''

import threading
import time
import random

n = 4

def barrier_action():
    print("四个人凑齐，游戏开始！")


barrier = threading.Barrier(parties=n, action=barrier_action)


def loading(player_id):
    # 模拟资源加载时间
    loading_time = round(random.uniform(1, 6), 2)
    time.sleep(loading_time)
    print("[玩家{}] 资源加载完成！耗时: {}s".format(player_id, loading_time))

    barrier.wait(60)  # 最多等待60秒，否则当掉线处理

    """后面就是具体的每个玩家进入游戏的代码了
    """
    print("[玩家{}] 进入游戏".format(player_id))


if __name__ == "__main__":
    threads = [threading.Thread(target=loading, args=(i,)) for i in range(n)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
