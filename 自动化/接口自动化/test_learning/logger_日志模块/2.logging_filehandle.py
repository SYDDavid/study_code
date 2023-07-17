'''
filehandler中若输出存在中文，需定义编码格式

'''
import logging

logger = logging.getLogger('syd_logger')
logger.setLevel(logging.INFO)

handle2 = logging.FileHandler('test_log.txt', encoding='utf-8')

fmt = ' %(msecs)d %(name)s %(levelname)s %(filename)s-%(lineno)d %(message)s'
formatter = logging.Formatter(fmt)

handle2.setFormatter(formatter)
logger.addHandler(handle2)

logger.error('error!!!')
