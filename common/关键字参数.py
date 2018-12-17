'''
关键字参数相当于传入一个字典
写法一
'''
def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)

person('jiang',23,city='chengdu',job='IT')

'''
写法二
'''
exta={'city':'shanghai','job':'IT'}
person('jian',23,**exta)