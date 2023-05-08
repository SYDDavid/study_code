### 进程和线程的区别

# 进程是运行着的程序，平时为.exe存储于磁盘中被os调用到内存中参与运算的程序
# 每一个进程至少包含一个线程，线程由操作系统创建，每个线程对应一个代码执行的数据结构
# 进程作为分配资源的基本单位，而把线程作为独立运行和独立调度的基本单位

# 多线程的好处：大量减少程序执行所消耗的时间

# 在python中对系统申请新的线程：threading库

import threading
import time

print('main initiate')


def subthreading(args1, args2):
    print('sub initiate')
    print(f'it has {args1},{args2}')
    time.sleep(5)
    print('sub finish')


subprocess = threading.Thread(
    target=subthreading,  # 对象获取函数地址，加上括号获取的为函数对象
    args=('参数1', '参数2')  # 函数的传参，需要依次填写，若只有一个参数元组内需要有逗号args=('参数1'，)
)

subprocess.start()  # 创建并启动子线程
subprocess.join()  # 这个方法会强制让子线程结束后再继续执行主线程下内容
print('main finish')

# 关于join函数，当线程A调用了线程B的join，就会停止A后续代码的执行，等待B执行完后继续A
# 通常这么设定的意义在于，多设置几个线程，等待它们处理完对其结果再进行分析

### 共享数据的访问控制

# 多线程同时访问一个资源时，常会引起冲突

from threading import Thread, Lock
from time import sleep

bank = {
    'byhy': 0
}

bankLock = Lock()


# 定义一个函数，作为新线程执行的入口函数
def deposit(theadidx, amount):
    # 操作共享数据前，申请获取锁
    bankLock.acquire()

    balance = bank['byhy']
    # 执行一些任务，耗费了0.1秒
    sleep(0.1)
    bank['byhy'] = balance + amount
    print(f'子线程 {theadidx} 结束')

    # 操作完共享数据后，申请释放锁
    bankLock.release()


theadlist = []
for idx in range(10):
    thread = Thread(target=deposit,
                    args=(idx, 1)
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('主线程结束')
print(f'最后我们的账号余额为 {bank["byhy"]}')

print('*' * 50)


# 当前理解为，对于每个不同锁，有且仅有一个，当线程遇到该锁时，优先查看锁是否为开启状态，若有必须进行等待，等候上一个使用锁的对象主动释放
# 根据以上逻辑，依次来保护公共资源，按时间来依次操作资源


### 守护线程（daemon threading）
# 1.daemon线程是指程序运行时，后台提供的服务线程
# 2.当所有非daemon线程结束时程序就会终止，并杀死所有daemon线程
# 3.在线程start之前，必须daemon=True，无法将一个正在执行的线程做守护处理
# 4.daemon的新线程也为daemon
# 5.daemon理论上不允许访问固有资源

def daemon():
    time.sleep(10)


Daemon = threading.Thread(
    target=daemon,
    daemon=True # 此处设置线程是否为守护线程
)

Daemon.start()

### 