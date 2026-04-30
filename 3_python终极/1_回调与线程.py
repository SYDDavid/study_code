# -*- coding: utf-8 -*-

'''
解决的工程问题：
    1、 解决“阻塞等待”问题：回调下支持同时处理不同的事情，结果将会单独被处理
    2、 解决“代码僵化”问题：主程序只需关心需要的时候提供什么，可以流程放权给下面的用户去实现，你只需要关心什么时候外抛东西出去
    3、 解决“条件轮询”问题：事假驱动思维避免了程序不断轮询判断条件，只需要时机合适即可执行接下来的操作
会出现的灾难和解决方案：
    回调地狱：多个异步操作有先后依赖关系时，你必须把下一步的操作嵌套在上一步的回调里
        解决方案：
        1、 Promise / Future：将嵌套的回调拉平成链式调用。
        2、 async / await：用同步的写法写异步的代码（底层依然是回调/状态机机制），这是目前主流语言最推崇的方案。
'''

import time
import threading


# =====================================================================
# 第一部分：定义回调函数
# =====================================================================

def on_download_success(file_name, file_size):
    """下载成功后的回调函数"""
    # 注意看这里：我们会打印当前执行这个函数的线程名字
    print(f"[回调执行] 恭喜！文件 {file_name} ({file_size}MB) 下载成功！")
    print(f"[回调执行] 当前执行线程: {threading.current_thread().name}")
    print("-" * 40)


def on_download_failure(file_name, error_msg):
    """下载失败后的回调函数"""
    print(f"[回调执行] 哎呀！文件 {file_name} 下载失败，原因: {error_msg}")
    print(f"[回调执行] 当前执行线程: {threading.current_thread().name}")
    print("-" * 40)


# =====================================================================
# 第二部分：模拟一个下载器
# =====================================================================

def download_file_sync(file_name):
    """【同步阻塞式下载】没有回调，死等"""
    print(f"[主线程] 开始同步下载 {file_name}...")
    time.sleep(2)  # 模拟下载耗时2秒，此时主线程卡死，什么都不干
    print(f"[主线程] {file_name} 下载结束！")
    return f"{file_name}_data"


def download_file_with_callback(file_name, success_callbacfailure_callback):
    """【带回调的异步下载】留下字条，立刻返回"""
    print(f"[子线程] 开始在后台下载 {file_name}...")

    # 模拟耗时的下载过程
    time.sleep(2)

    # 下载完成，根据结果决定调用哪个“字条（回调）”
    if "机密" in file_name:
        # 模拟下载失败的情况，触发失败回调
        error_msg = "权限不足，无法获取"
        failure_callback(file_name, error_msg)
    else:
        # 模拟下载成功的情况，触发成功回调
        file_size = 1024
        # ? 核心动作：在这里“回调”你传进来的函数！
        success_callback(file_name, file_size)

    print(f"[子线程] {file_name} 后台任务收尾完毕。")


# =====================================================================
# 第三部分：主程序运行
# =====================================================================

if __name__ == "__main__":
    print("=== 1. 同步阻塞式下载（没有回调）===")
    print(f"[主线程] 当前线程: {threading.current_thread().name}")
    start_time = time.time()

    # 同步调用：主线程必须等 download_file_sync 执行完（等2秒），才能往下走
    result = download_file_sync("报告.docx")
    print(f"[主线程] 拿到结果: {result}，继续干别的事...")
    print(f"[主线程] 同步方式总耗时: {time.time() - start_time:.2f}秒\n")

    print("=== 2. 异步回调式下载（使用回调）===")
    print(f"[主线程] 当前线程: {threading.current_thread().name}")
    start_time = time.time()

    # 异步调用：开启一个新线程去下载，并把回调函数（字条）传进去
    # target: 子线程要执行的函数
    # args:   传给子线程函数的参数，这里我们把 on_download_success 和 on_download_failure 当作参数传了过去！
    thread1 = threading.Thread(
        target=download_file_with_callback,
        args=("照片.jpg", on_download_success, on_download_failure)
    )

    thread2 = threading.Thread(
        target=download_file_with_callback,
        args=("机密档案.zip", on_download_success, on_download_failure)
    )

    # 启动线程，主线程立刻继续往下走，不会被阻塞2秒
    thread1.start()
    thread2.start()

    print(f"[主线程] 任务已委派给子线程，我不用干等，可以去喝咖啡了~")
    print(f"[主线程] 异步委派耗时: {time.time() - start_time:.2f}秒 (几乎不耗时)")

    # 主线程等待子线程结束（只是为了防止主程序退出看不到打印结果）
    # 如果不 join，主线程继续往下走，可能程序就直接退出了
    thread1.join()
    thread2.join()

    print(f"[主程序] 全部任务彻底结束。")
