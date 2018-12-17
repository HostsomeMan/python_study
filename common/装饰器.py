import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

'''
    把@log放到now函数定义处，相当于执行了语句：now=log(now)
'''
@log
def now():
    print('2018-12-05')

f = now
f()
print(f.__name__)