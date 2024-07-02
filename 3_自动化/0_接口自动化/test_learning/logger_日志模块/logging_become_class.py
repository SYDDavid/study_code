'''
封装完成后，需注意：
    1、别的文件内调用尽量从项目目录下开始import
    2、输出方式为。logger.等级
    3、存在一种输出所有错误信息的方式：logger.exception
'''

import logging
import os


class SYD_logger(logging.Logger):

    def __init__(self, logger_name, level=logging.INFO, file_name=None):
        super().__init__(logger_name, level)

        # 设定日志输出格式
        fmt = ' %(msecs)d %(name)s %(levelname)s %(filename)s-%(lineno)d %(message)s'
        formatter = logging.Formatter(fmt)

        if file_name:
            handle2 = logging.FileHandler(file_name, encoding='utf-8', mode='w')
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
        else:
            handle1 = logging.StreamHandler()
            handle1.setFormatter(formatter)
            self.addHandler(handle1)


abs_path = os.path.abspath(__file__)
abs_dirname_path = os.path.dirname(abs_path)
abs_log_path = os.path.join(abs_dirname_path, 'test_log.txt')

my_logger = SYD_logger('syd_log', file_name=abs_log_path)

if __name__ == '__main__':
    my_logger = SYD_logger('syd_log', file_name='test_log.txt')
    my_logger.error("error")
