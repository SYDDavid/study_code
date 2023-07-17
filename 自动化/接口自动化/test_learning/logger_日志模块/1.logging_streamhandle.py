'''
logging模块
    0、日志名字
    1、日志级别(Level)：DEBUG/INFO/WARNING/ERROR/CRITICAL(FATAL)
    此处使用时需注意logging.XXX
    2、输出渠道(Handle)：控制台(streamHandle)、文件(fileHandle)
    3、日志内容(Formatter)：时间、哪个文件、哪行代码、输出内容

第一步：创建一个日志收集器           logging.getLogger('XXX')
第二步：设置日志级别                logger.setLevel(logging.INFO)
第三步：设置输出渠道                loggging.StreamHandle()
第四步：设置日志内容                设定输出格式fmt、再logging.Formatter
第五步：绑定内容与渠道               .setFormatter(fmt)
第六步：绑定渠道与收集器             .addHandler(hdlr)

总结思路：

日志收集器（logger） => 渠道（handle） => 输出格式（formatter）
可自定义输出级别         可自定义输出级别

理解：可以设定多渠道，多格式，按照需求定制化输出

'''

import logging

logger = logging.getLogger('syd_logger')

logger.setLevel(logging.INFO)

# 设置日志输出渠道
handle1 = logging.StreamHandler()

# 设置日志格式
fmt = ' %(msecs)d %(name)s %(levelname)s %(filename)s-%(lineno)d %(message)s'
formatter = logging.Formatter(fmt)

# 将日志输出格式与渠道做绑定
handle1.setFormatter(formatter)

# 将渠道与日志收集器做绑定
logger.addHandler(handle1)

logger.info('info')
logger.error('error')

# 渠道也可以设置级别！！！！
handle1.setLevel(logging.ERROR)
logger.info('info')
logger.error('error')
