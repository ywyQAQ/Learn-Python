# 全局解释器锁，担心它会影响到多线程程序的执行性能

# 解释器的C语言实现部分在完全并行执行的时候并不是线程安全的。
# 实际上，解释器被一个大局解释器锁保护着，它确保任何时候都只有一个Python线程执行。
# GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势
# 比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行

# 在讨论普通的GIL之前，有一点要强调的是GIL只会影响到哪些严重依赖CPU的程序。
# 如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程很合适，因为大部分时间都在等待。
# 而对于依赖CPU的程序，你需要弄清楚执行的计算的特点。例如，优化底层算法比使用多线程裕兴快得多。
# 类似的，由于Python是解释执行的，如果你将那些性能瓶颈代码移到一个C语言扩展模块中， 速度也会提升的很快。
# 如果你要操作数组，那么使用NumPy这样的扩展会非常的高效。 
# 最后，你还可以考虑下其他可选实现方案，比如PyPy，它通过一个JIT编译器来优化执行效率 （不过在写这本书的时候它还不能支持Python 3）。

# 而且还有一点要注意的是，线程不是专门用来优化性能的。一个CPU依赖型程序可能会使用线程来管理一个图形用户界面、一个网络连接或其他服务。
# 这时候GIL会产生一些问题，因为如果一个线程长期持有GIL的话，会导致其他非CPU型线程一直等待。
# 事实上，一个写的不好的C语言拓展会导致这个问题更加严重，尽管代码的计算部分会比之前快很多。

# 两个策略来解决GIL的缺点。首先，如果完全工作在Python环境中，你可以使用multiprocessing模块来创建一个进程池，
# 并像协同处理器一样的使用它。例如，假如你有如下的线程代码：

# Performs a large calculation (CPU bound)
def some_work(args):
    ...
    return result

# A thread that calls the above function
def some_thread():
    while True:
        ...
        r = some_work(args)

# 修改代码，使用进程池：
# Processing pool (see below for initiazation)
pool = None

# Performs a large calculation (CPU bound)
def some_work(args):
    ...
    return result

# A thread that calls the above function
def some_thread():
    ...
    r = pool.apply(some_work, (args))
    ...

# Initalize the pool
if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()

# 这个通过使用一个技巧利用进程池解决了GIL的问题。 当一个线程想要执行CPU密集型工作时，会将任务发给进程池。 
# 然后进程池会在另外一个进程中启动一个单独的Python解释器来工作。 当线程等待结果的时候会释放GIL。 
# 并且，由于计算任务在单独解释器中执行，那么就不会受限于GIL了。 在一个多核系统上面，你会发现这个技术可以让你很好的利用多CPU的优势。

# 另外一个解决GIL的策略是使用C扩展编程技术。 
# 主要思想是将计算密集型任务转移给C，跟Python独立，在工作的时候在C代码中释放GIL。 
# 这可以通过在C代码中插入下面这样的特殊宏来完成：

#include "Python.h"
...

PyObject *pyfunc(PyObject *self, PyObject *args) {
   ...
   Py_BEGIN_ALLOW_THREADS
   // Threaded C code
   ...
   Py_END_ALLOW_THREADS
   ...
}
# 如果你使用其他工具访问C语言，比如对于Cython的ctypes库，你不需要做任何事。 例如，ctypes在调用C时会自动释放GIL。
