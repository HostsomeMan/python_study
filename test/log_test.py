from common import logger

logger = logger.mylog('test').getlog()

try:
    logger.info('开始测试')
    r = 10/0
    logger.info('result',r)
except ZeroDivisionError as e:
    logger.error('tests',exc_info=1)

logger.info('end')