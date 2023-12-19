# 实现一个自定义迭代模式，跟普通的内置函数比如range(), reversed()不一样。

# 如果想实现一种新的迭代模式，使用一个生成器函数来定义它。下面是一个生产某个范围内浮点数的生成器：

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x 
        x += increment

# 为了使用这个函数，你可用for循环迭代它或者使用其他接受一个可迭代对象的函数(比如sum()，list()等、)

for n in frange(0, 4, 0.5):
    print(n)




list(frange(0, 1, 0.125))

# 一个函数需要有一个yield语句即可将其转换为一个生成器。跟普通函数不同的是，生成器只能用于迭代操作。

# 一个生成器函数主要特征是它只会回应在迭代中使用到的next操作。一旦生成器函数返回退出,迭代终止。
def countdown(n):
    print('Starting to count from', n)
    while n  > 0:
        yield n
        n -= 1
    print('Done!')
