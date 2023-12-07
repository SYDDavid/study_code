'''
为了让代码更简短简洁，又为了可以防止遗忘，本来原子层的锁与释放可以这么写：
    lock.acquire()
    lock.release()
现，可以修改为：
    with lock:
'''

# 顺序控制：优先执行A.print再B.print

from threading import Lock, RLock, Condition, Semaphore, Thread

# def print_a():
#     print('this is a')
#
# def print_b():
#     print('this is b')
#
# def main():
#     thread_A = Thread(target=print_a)
#     thread_B = Thread(target=print_b)
#
#     thread_B.start()
#     thread_A.start()
#
#     thread_B.join()
#     thread_A.join()
#
# if __name__ == '__main__':
#     main()
lock = Lock()
lock.acquire()


def print_a():
    print('this is a')
    lock.release()


def print_b():
    lock.acquire()
    print('this is b')


def main():
    thread_A = Thread(target=print_a)
    thread_B = Thread(target=print_b)

    thread_B.start()
    thread_A.start()

    thread_B.join()
    thread_A.join()


if __name__ == '__main__':
    main()
