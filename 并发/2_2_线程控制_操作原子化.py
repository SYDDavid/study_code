'''
两个线程公用同一资源，若资源非单例，两个线程操作各自镜像后重赋值，来达到修改目的，会导致最终结果只保留最后一笔提交记录

对两个独立事务，又要处理同一资源，加锁已确保事件按序完成
'''
from threading import Lock, RLock, Condition, Semaphore, Thread
import time
#
# balance = 100
#
# def save100():
#
#     global balance
#     current_balance = balance
#     left_balance = current_balance + 100
#     time.sleep(1)           # 假设写回数据库需要1秒
#     balance = left_balance
#
# def withdraw20():
#
#     global balance
#     current_balance = balance
#     left_balance = current_balance - 20
#     time.sleep(1)           # 假设写回数据库需要1秒
#     balance = left_balance
#
# if __name__ == "__main__":
#     thread_A = Thread(target=save100)
#     thread_B = Thread(target=withdraw20)
#
#     thread_B.start()
#     thread_A.start()
#
#     thread_B.join()
#     thread_A.join()
#
#     print("balance :", balance)
balance = 100
lock = Lock()

def save100():
    with lock:
        global balance
        current_balance = balance
        left_balance = current_balance + 100
        time.sleep(1)           # 假设写回数据库需要1秒
        balance = left_balance


def withdraw20():
    with lock:
        global balance
        current_balance = balance
        left_balance = current_balance - 20
        time.sleep(1)           # 假设写回数据库需要1秒
        balance = left_balance


if __name__ == "__main__":
    thread_A = Thread(target=save100)
    thread_B = Thread(target=withdraw20)

    thread_B.start()
    thread_A.start()

    thread_B.join()
    thread_A.join()

    print("balance :", balance)