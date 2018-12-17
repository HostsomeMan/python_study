'''
    可变参数：
    传入列表或元祖
    在方法参数前加*

'''
def calc(*number):
    sum = 0
    for i in number:
        sum = sum+i*i
    return sum

print(calc(*[1,2,3,4]))
print(calc(9,8,2))

'''

'''

def calc1(number):
    sum = 0
    for i in number:
        sum = sum+i*i
    return sum

print(calc1([1,2,3,4]))


'''
    关键字参数

'''

