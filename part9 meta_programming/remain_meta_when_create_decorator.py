# 写一个装饰器作用在某个函数上，但是这个函数的重要元信息比如名字、
# 文档字符串、注解和参数签名都丢失了。

# 任何时候你定义装饰器的时候，都应该使用functools库中的@wraps装饰器包装函数。、
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
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

# 使用这个被包装后的函数并检查它的元信息：
@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1
print(countdown(100000))
# countdown 0.004044294357299805
print(countdown.__name__)
# 
print(countdown.__doc__)
#
print(countdown.__annotations__)
# 

# @wraps有一个重要特征是它能让你通过__wrapped__直接访问被包装函数。
countdown.__wrapped__(100000)

# __wrapped__属性还能让被装饰器正确暴露底层的参数签名信息。例如：
from inspect import signature
print(signature(countdown))
