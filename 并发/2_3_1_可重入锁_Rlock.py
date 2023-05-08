'''
Rlock是可重入锁，即：可反复进行锁操作，内部会记录acquire次数，若这个次数为n，那么就需要releaseN次来彻底释放这个锁
'''
from threading import Lock, RLock, Condition, Semaphore, Thread
import time

# lock = Lock()
lock = RLock()


def A():
    with lock:
        print("I am A and to invoke B")
        # 这里的A先acquire，调用B的acquire，但B的lock需要先等待A的release，然而A的release再B后，导致B无限等待，最终死锁
        # 修改为rlock即可避免该问题
        B()


def B():
    with lock:
        print("I am B")


if __name__ == "__main__":
    thread_A = Thread(target=A)
    thread_B = Thread(target=B)

    thread_A.start()
    thread_B.start()

    thread_A.join()
    thread_B.join()
