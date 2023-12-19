# 让对象支持上下文管理协议(with语句)

# 为了让一个对象兼容with语句，你需要实现__enter__()和__exit__()方法。
# 例如，考虑如下的一个类，它能为我们创建一个网络连接：

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM) -> None:
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
    
    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
    
# 使用with语句自动完成连接的建立和关闭。
# 无论with代码块发生什么，上面的控制流都会执行完，就算代码块中发生了异常也是一样的。
# 事实上，__exit__()方法的三个参数包含了异常类型、异常值和追溯信息（如果有的话）。
# __exit__()方法能自己决定怎样利用这个异常信息，或者忽略它并返回一个None值。
# 如果__exit__()返回True，那么异常会被清空，就好像什么都没发生一样，with语句后面的程序继续在正常运行。

# LazyConnection类是否允许许多个with语句来嵌套使用连接。
# 很明显，上面的定义只允许一个socket连接，再重复使用with会产生一个异常。
# 不过可以像下面这样修改下上面的实现来解决这个问题。

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

# Example use
from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
        # s1 and s2 are independent sockets


# 在第二个版本中，LazyConnection 类可以被看做是某个连接工厂。
# 在内部，一个列表被用来构造一个栈。 每次 __enter__() 方法执行的时候，
# 它复制创建一个新的连接并将其加入到栈里面。 __exit__() 方法简单的从栈中弹出最后一个连接并关闭它。 
# 这里稍微有点难理解，不过它能允许嵌套使用 with 语句创建多个连接，就如上面演示的那样。

# 在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。 
# 这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行。 
# 例如，如果你请求了一个锁，那么你必须确保之后释放了它，否则就可能产生死锁。 
# 通过实现 __enter__() 和 __exit__() 方法并使用 with 语句可以很容易的避免这些问题， 
# 因为 __exit__() 方法可以让你无需担心这些了。

# 在 contextmanager 模块中有一个标准的上下文管理方案模板，可参考9.22小节。 
# 同时在12.6小节中还有一个对本节示例程序的线程安全的修改版。