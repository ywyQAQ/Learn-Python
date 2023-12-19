# 一个装饰器已经作用在一个函数上，想撤销它，直接访问原始的未包装的哪个函数。

# 假设装饰器是通过@wraps（参考9.2）来实现的，那么可以通过范文__wrapped__属性访问原始函数：

@somedecorator
def add(x, y):
    return x + y

orig_add = add.__wrapped__
orig_add(3, 4)

# 直接访问未包装的原始函数在调试、内省和其他函数操作时是很有用的。

# 如果有多个包装器，那么访问__wrapped__属性的行为是不可预知的，应该避免这样的操作。
# 在python3.3中，它会略过所有的包装层、

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

# 下面在Python3.3下测试：
add(2, 3)
Decorator 1
Decorator 2
5
add.__wrapped__(2, 3)
5

# 下面在Python3.4下测试：
Decorator 1
Decorator 2
5
add.__wrapped__(2, 3)
Decorator 2
5

#　最后要说的是，并不是所有的装饰器都使用了 @wraps ，因此这里的方案并不全部适用。 
# 特别的，内置的装饰器 @staticmethod 和 @classmethod 就没有遵循这个约定 
# (它们把原始函数存储在属性 __func__ 中)。