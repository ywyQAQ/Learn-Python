# 定义带参数的装饰器

# 用一个例子详细阐述下接受参数的处理过程。
# 以下是一个给函数添加日志功能，同时允许用户指定日志的级别和其他的选项。

from functools import wraps
import logging

def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

# 乍看起来很复杂，但是核心思想很简单。最外层的logged()接受参数并将它们
# 作用在内部的装饰器上面。内层的函数decorate()接受一个函数作为参数，然后在函数上放置一个包装器。
# 这里的关键点是包装器是可以使用传递给logged()的参数的。

@decorator(x, y, z)
def func(a, b):
    pass
# 等同于

def func(a, b):
    pass
func = decorator(x, y, z)(func)
# decorator(x, y, z)的返回结果必须是一个可调用对象，它接受一个参数作为参数并包装它。
