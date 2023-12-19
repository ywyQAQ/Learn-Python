# 需要保存正在运行线程的状态，这个状态对于其他线程不可见

# 有时在多线程编程中，你需要只保存当前运行线程的状态。要这么做，可使用thread.local()
# 创建一个本地线程存储对象。对这个对象的属性的保存和读取操作都只会对执行线程可见，而其他线程并不可见。
# 8.3节定义过的LazyConnection上下文管理器类。下面我们对它进行一些小的修改使得它可以适用于多线程。

from socket import socket, AF_INET, SOCK_STREAM
import threading

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM) -> None:
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()
    
    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected!')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock
    
    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock

# 代码中，自己观察对于self.local的使用，被初始化为一个threading.local()实例。
# 其他方法操作被存储为self.lock.sock的套接字对象，安全地使用LazyConnection实例，例如：

from functools import partial
def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')

        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))

    print('Got {} bytes'.format(len(resp)))

if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))

    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 一些专用的系统资源，比如套接字或文件。你不能让所有线程共享一个单独对象，因为多个线程同时读和写会产生混乱。

# 之所以行得通的原因是每个线程会创建一个自己专属的套接字连接(存储为self.lock.sock)
# 在本节中，使用thread.local()可以让LazyConnection类支持一个线程一个连接，而不是所有的进程一个连接。
# 原理是，每个threading.local()实例为每个线程维护者一个单独的实例字典。所有普通实例操作比如获取、修改和删除值仅仅操作这个字典、
# 每个线程使用一个独立的字典就可以保证数据的隔离了。
