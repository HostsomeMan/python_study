#-*-coding:utf-8-*-

'''
Created on 2018��12��12��

@author: Administrator
'''
import logging

'''
    默认级别是logging.warning，低于该级别的就不输出了
    设置日志级别，需要大写
'''
logging.basicConfig(level=logging.DEBUG)# 设置日志级别，需要大写
# logging.debug("a")
# logging.info("b")
# logging.warning('c')
# logging.error('d')
# logging.critical('e')

'''
    logger类
        logging模块定义的模块级别函数
            函数 	说明
            logging.debug(msg, *args, **kwargs)         创建一条严重级别为DEBUG的日志记录
            logging.info(msg, *args, **kwargs)          创建一条严重级别为INFO的日志记录
            logging.warning(msg, *args, **kwargs)       创建一条严重级别为WARNING的日志记录
            logging.error(msg, *args, **kwargs)         创建一条严重级别为ERROR的日志记录
            logging.critical(msg, *args, **kwargs)      创建一条严重级别为CRITICAL的日志记录
            logging.log(level, *args, **kwargs)         创建一条严重级别为level的日志记录
            logging.basicConfig(**kwargs)               对root logger进行一次性配置

        logging模块的四大组件
            组件名称     对应类名     功能描述
            日志器     Logger          提供了应用程序可一直使用的接口
            处理器     handler         将logger创建的日志记录发送到合适的目的输出
            过滤器     Filter          提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
            格式器     Formatter       决定日志记录的最终输出格式
        组件之间的关系描述：
            日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；不同的处理器（handler）可以将日志输出到不同的位置；
            日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
            每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
            每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。
            简单点说就是：日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和
            +格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。

'''

# a = logging.getLogger("mylogger")             # 设置传入日志的名称，并将对象赋值给a，用a来调用相应方法
# a.setLevel(logging.INFO)                      # 通过setLeverl()方法设置logger的日志输出级别
# a.debug("a")
# a.info("b")
# a.warning('c')
# a.error('d')
# a.critical('e')

'''
    handler类
        通过handler对象可以把日志内容写到不同地方，python提供了十几种实用的handler，比较常用的有：
        类型 	说明
        StreamHandler               输出到控制台
        FileHandler                 输出到文件
        BaseRotatingHandler         可以按时间写入到不同的日志中。比如将日志按天写入不同的日期结尾的文件文件
        SocketHandler               用TCP网络连接写LOG
        DatagramHandler             用UDP网络连接写LOG
        SMTPHandler                 把LOG写成EMAIL邮寄出去
'''
fh = logging.FileHandler('D:/test1.txt')            # 创建一个输出到指定文件的handler对象fh
a = logging.getLogger("MyRoot")
fh.setLevel(logging.INFO)                             # 设置日志级别
a.addHandler(fh)                                      # 给logger添加handler
# a.info("这个日志有点扯把子")

'''
    handler常用方法
        Handler.setLevel()                              设置handler将会处理的日志消息的最低严重级别
        Handler.setFormatter()                          为handler设置一个格式器对象
        Handler.addFilter() 和 Handler.removeFilter()    为handler添加 和 删除一个过滤器对象
    Formater类
        字段/属性名称 	使用格式 	描述
        asctime 	%(asctime)s 	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
        created 	%(created)f 	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
        relativeCreated 	%(relativeCreated)d 	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
        msecs 	%(msecs)d 	        日志事件发生事件的毫秒部分
        levelname 	%(levelname)s 	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
        levelno 	%(levelno)s 	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
        name 	%(name)s 	        所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
        message 	%(message)s 	日志记录的文本内容，通过 msg % args计算得到的
        pathname 	%(pathname)s 	调用日志记录函数的源码文件的全路径
        filename 	%(filename)s 	pathname的文件名部分，包含文件后缀
        module 	%(module)s 	filename的名称部分，不包含后缀
        lineno 	%(lineno)d 	调用日志记录函数的源代码所在的行号
        funcName 	%(funcName)s 	调用日志记录函数的函数名
        process 	%(process)d 	进程ID
        processName 	%(processName)s 	进程名称，Python 3.1新增
        thread 	%(thread)d 	线程ID
        threadName 	%(thread)s 	线程名称

'''
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   # 配置日志输出格式
fh.setFormatter(formatter)  # 给handle加上格式
a.info('1244555')

b = logging.getLogger("MyKing")
b.setLevel(logging.INFO)
bh = logging.StreamHandler()            # 输出到控制台
bh.setFormatter(formatter)              # 将给handler添加格式规则
b.addHandler(bh)                        # 给b添加handler对象
b.info('输出到控制台')



