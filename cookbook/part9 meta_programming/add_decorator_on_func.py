# 在函数上添加一个包装器，增加额外的操作处理（比如日志、计时）

# 定义一个装饰器函数

import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end  = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

# 下面是使用装饰器的例子
@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

# 一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数。当你像下面这样写：
@timethis
def countdown(n):
    pass

# 跟下面这样写其实效果是一样的

def countdown(n):
    pass

countdown = timethis(countdown)

# 顺便说一下，内置的装饰器比如
# @staticmethod, @classmethod, @property原理是一样的。

# 上面的wrapper()函数中，装饰器内部定义了一个使用*args和**kwargs来接受任意参数的函数。
# 在这个函数里面调用了原是函数并将其结果返回。

# 需要强调的是装饰器并不会修改原始函数的参数签名以及返回值。
# 有一些细节问题要注意的，比如@wraps(func)注解是非常重要的，它能保留原始函数的原数据。