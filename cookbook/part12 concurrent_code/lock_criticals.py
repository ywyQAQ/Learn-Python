# 需要给多线程程序中的临界区加锁以避免竞争条件。

# 要在多线程程序中安全使用可变对象，你需要使用threading库中的Lock对象。

import threading

class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()
    
    def incr(self, delta=1):
        '''
        Increament the counter with locking
        '''
        with self._value_lock:
            self._value += delta
    
    def decr(self, delta=1):
        '''
        Decrement the counter with locking
        '''
        with self._value_lock:
            self._value -= delta

# Lock对象和with语义块一起使用可以保证互斥执行，就是每次只有一个线程可以执行with语句包含的代码块。

# 为了避免出现死锁的情况，使用锁机制的程序应该设定为每个线程一次只允许获取一个锁。如果不能这样做，
# 就需要更高等级的死锁避免机制，我们将在下一章avoid_death_lock中讨论。

# 在threading库中还提供了其他的同步原语，比如RLock和Semaphore对象。这些原语是用在一些特殊情况。
# 如果你只是简单地对可变对象进行锁定，那么就不应该用它们。
# 一个RLock（可重入锁）可以被同一个线程多次获取，主要用来实现基于检测对象模式的锁定合同部。
# 在使用这种锁的情况下，当锁被持有时，只有一个线程可以使用完整的函数或类中的方法。比如，
import threading

class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    _lock = threading.RLock()
    def __init__(self, initial_value = 0):
        self._value = initial_value

    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        with SharedCounter._lock:
            self._value += delta

    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with SharedCounter._lock:
             self.incr(-delta)

# 在这个例子中，没有对每一个实例中的可变对象加锁，取而代之的是一个被所有实例共享的类级锁。
# 这个锁用来同步类方法，具体来说就是，这个锁可以保证一次只有一个线程可以调用这个类方法。
# 不过与一个标准的锁不同的是，已经持有这个锁的方法在调用同样适用这个锁的方法时不需要再获取锁。
# 比如decr方法，这种实现的特点是，无论这个类有多少个实例都只用一个锁。
# 因此在需要大量使用计数器的情况下内存效率更高。不过这样做也有缺点，
# 就是在程序中使用大量线程并频繁更新计数器时会有争用锁的问题。 
# 信号量对象是一个建立在共享计数器基础上的同步原语。
# 如果计数器不为0，with 语句将计数器减1，线程被允许执行。
# with 语句执行结束后，计数器加１。如果计数器为0，线程将被阻塞，直到其他线程结束将计数器加1。
# 尽管你可以在程序中像标准锁一样使用信号量来做线程同步，但是这种方式并不被推荐，
# 因为使用信号量为程序增加的复杂性会影响程序性能。相对于简单地作为锁使用，
# 信号量更适用于那些需要在线程之间引入信号或者限制的程序。
# 比如，你需要限制一段代码的并发访问量，你就可以像下面这样使用信号量完成：

from threading import Semaphore
import urllib.request

# At most, five threads allowed to run at once
_fetch_url_sema = Semaphore(5)

def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)
    
# RLOCK解决递归中的锁问题。

def example_function(lock):
    with lock:
        print("Inside critical section")
        # 在已经获取锁的情况下再次获取锁
        with lock:
            print("Inside nested critical section")

if __name__ == "__main__":
    rlock = threading.RLock()

    # 创建两个线程，分别执行 example_function
    thread1 = threading.Thread(target=example_function, args=(rlock,))
    thread2 = threading.Thread(target=example_function, args=(rlock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()