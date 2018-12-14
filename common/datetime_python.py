#-*-coding:utf-8-*-
from datetime import datetime, timedelta

mow = datetime.now()
print(mow)
print(type(mow))

dt = datetime(2018,10,26,12,45,23)
print(dt)
# 将datetime转换为timestamp
ts = dt.timestamp()
print(ts)
# 将timestamp转换为datetime
'''
    使用fromtimestamp()可将timestamp转换成本地时间
    使用utcfromtmestamp()可将timestamp转成成utc时间
    因为北京是utc+8:00，所以utc时间会减少八小时
'''
print(datetime.fromtimestamp(ts))
print(datetime.utcfromtimestamp(ts))

# str转换为datetime，使用strptime()方法
times = "2018-10-26 15:23:56"
print(type(times))
print(type(datetime.strptime(times, '%Y-%m-%d %H:%M:%S')))

# datetime转换为str 使用strftime()方法
str = datetime.now()
print(str)
print(datetime.strftime(str, '%Y-%m-%d %H:%M:%S'))

# datetime加减
new_time = datetime.now()
print(new_time+timedelta(days=2, hours=1))

