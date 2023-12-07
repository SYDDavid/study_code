'''
猜想：rlock.acquire会先查询锁情况：
        1、rlock在代码块内，可执行
        2、rlock在代码块外，若未被占，可执行；若已被占，等待释放
    关于rlock.release：
        需在对应代码块内释放
'''

from threading import Lock, RLock, Condition, Semaphore, Thread
import time

lock = RLock()
lock.acquire()

def A():
    lock.acquire()
    print('this is A')
    lock.release()


def B():
    lock.acquire()
    print('this is B')
    lock.release()


def main():
    thread_A = Thread(target=A)
    thread_B = Thread(target=B)

    thread_B.start()
    thread_A.start()

    thread_B.join()
    thread_A.join()


if __name__ == '__main__':
    main()
