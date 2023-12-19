# 需要为并发执行的代码创建/销毁线程。
# threading库可以在单独的线程里执行任何的在Python中可以调用的对象。
# 你可以创建一个Thread对象并将你要执行的对象以target参数的形式提供给该对象。

# Code to execute in an independent thread
import socket
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create and Launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

# 当你创建一个线程对象后，该对象并不会立即执行，除非你调用start()方法。
# Python中的线程会在一个单独的系统级线程中执行（比如一个POSIX线程或者一个Windows线程）
# 这些线程将由操作系统全权管理。线程一旦执行，将独立执行直到目标函数返回。
# 还可以查询一个线程对象的状态，看它是否还在执行：
if t.is_alive:
    print('Still running')
else:
    print('Completed')

# 也可以将一个线程加入到当前线程，并等待它停止：
t.join()

# Python解释器直到所有线程都终止前仍保持运行。
# 对于需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程。例如：

t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
# 后台进程无法等待。不过这些线程会在主线程终止时自动销毁。
# 除了上述两个操作，并没有太多可以对线程做的事情。
# 你无法结束一个线程，无法向它发送信号，无法调整它的调度，也无法执行其他高级操作。
# 如果需要这些特性，需要自己添加。比如说，如果你需要终止线程，
# 那么这个线程必须通过编程在某一个特定点轮询来推出。你可以像下面这样把线程放入一个类中：
class CountdownTask:
    def __init__(self) -> None:
        self._running = True
    
    def terminate(self):
        self._running = False
    
    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate() # Signal termination
t.json() # wait for actual termination (if needed)

# 如果线程执行一些像I/O的阻塞操作，那么通过轮询来终止线程会变得很棘手。
# 比如一个线程如果一直阻塞在一个IO操作，它将永远不能返回，
# 也就是无法检查自己是否结束了。要正确处理这个问题，需要利用超时循环小心操作线程。
class IOTask:
    def terminate(self):
        self._running = False
    
    def run(self, sock):
        # sock is a socket
        sock.settimeout(5) # set timeout period
        while self._running:
            # Perform a blocking I/O operation timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
        return 

 # 由于全局解释锁(GIL)的原因，Python的线程被限制到同一时刻只允许一个线程
 # 执行这样的执行模型。所以，Python的线程更适用于处理IO和其他需要并发执行的阻塞操作，
 # （比如等待IO，等待从数据库获取数据等等），而不是需要多处理器并行的计算密集型任务。
 # 有时，你会看到下边这种通过继承Thread类来实现的线程：

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
    
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
        
c = CountdownThread(5)
c.start()
