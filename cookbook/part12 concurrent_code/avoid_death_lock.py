# 正在写一个多线程程序，其中线程需要一次获取多个锁，此时如何避免死锁问题。

# 死锁问题很大一部分是由于线程同时获取多个锁造成的。
# 解决死锁问题的一种方案是为程序中每一个锁分配一个唯一的id，然后只允许按照升序规则来使用多个锁。
# 这个规则使用上下文管理器是很容器实现的。

import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))
    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]

# 被contextmanager修饰的函数可以使用with语句，yield之前的部分用于在进入with语句块之前执行代码
# yield语句后的部分用于在退出with语句块时执行一些代码。
# _local变量是使用threading.local()创建的线程本地存储对象。
# 在多线程环境中，每个线程都有自己的独立的_local实例，并且这个实例是线程私有的，不会被其他线程访问到。

# 如何使用这个上下文管理器呢？你可以按照正常途径创建一个锁对象，但无论是单个锁还是多个锁都使用
# acquire()函数来申请锁，示例如下：

import threading
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')
    
def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()

# 执行这段代码，你会发现即使在不同的函数中以不同的顺序获取锁也没有发生死锁。
# 其关键在于，我们进行了排序。如果有多个acquire()操作被嵌套调用，
# 可以通过线程本地存储TLS来检测潜在的死锁问题。假设，你的代码是这样写的。
import threading
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():

    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')

def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()

# 如果你运行这个版本的代码，必定会有一个线程发生崩溃，异常信息可能像这样
# 发生崩溃的原因在于，每个线程都记录着自己已经获取到的锁。 
# acquire() 函数会检查之前已经获取的锁列表， 
# 由于锁是按照升序排列获取的，所以函数会认为之前已获取的锁的id必定小于新申请到的锁，
# 这时就会触发异常。

# 一旦有线程同时申请多个锁，一切就不可预料了。
# 一个比较常用的死锁检测和恢复方案是引入看门狗计数器。当线程正常运行的时候，会隔一段时间重置计数器。
# 一旦发生死锁，由于无法重置计数器导致定时器超时，这时程序会通过重启自身恢复到正常状态。
# 避免死锁是另一种解决死锁问题的凡是，在进程获取锁的时候会严格按照对象id升序排序。