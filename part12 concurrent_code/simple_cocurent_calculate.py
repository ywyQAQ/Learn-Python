# 一个程序要执行CPU密集型工作，你想让他利用多核CPU的优势来运行得快一些。

# concurrent.futures库提供了一个ProcessPoolExecutor类，可被用来在一个单独的Python解释器中执行计算密集型函数。
# 不过，要使用它，你首先要有一些任务。通过一个简单的例子来演示它。
# 下面是一个脚本，在这些日志文件中查找出所有访问过robots.txt文件的主机：
import gzip
import io
import glob


def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots

def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots

if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)

# 前面的程序使用了map-reduce风格来编写。函数find_robots()在一个文件名集合上做map操作，
# 并将结果汇总为一个单独的结果，也就是find_all_robots函数中的all_robots集合。现在，
# 假设你想修改这个程序让它使用多核CPU。很简单——只需要把map操作替换成concurrent.futures库里生成的类似操作即可。
# 下面是一个简单的修改版本：



import gzip
import io
import glob
from concurrent import futures

def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file

    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots

def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots

if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)



# ProcessPoolExecutor的典型用法如下：
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    do work in parallel using pool


# 其原理是，一个ProcessPoolExecutor创建N个独立的Python解释器，N是系统上面可用的CPU的个数。
# 可以通过提供可选参数给ProcessPoolExecutor(N)来修改处理器数量。这个处理池会一直运行到with块
# 中最后一个语句执行完成，然后处理池被关闭。不让过程序会一直等待直到所有提交的工作被处理完成。

# 被提交到池中的工作被定义为一个函数。有两种方法去提交，如果你想让一个列表推导或一个map()操作并行执行的话，
# 可使用pool.map()

def work(x):
    ...
    return result

# Parallel implementation
with ProcessPoolExecutor() as pool:
    results = pool.map(work, data)

# 另外，也可以使用pool.submit()来手动的提交单个任务：
# Some function
with ProcessPoolExecutor as pool:
    future_result = pool.submit(work, arg)

    # Obtain the result (blocks until done)
    r = future_result.result()

# 手动提交一个任务，结果是Future实例。要获取最终结果，需要调用result()方法。会阻塞进程直到结果返回。
# 如果不想阻塞，还可以使用一个回调函数

def when_done(r):
    print('Got:', r.result)

with ProcessPoolExecutor() as pool:
    future_result = pool.submit(work, arg)
    future_result.add_done_callback(when_done)

# 回调函数接受一个Future实例，被用来获取最终的结果(比如通过调用它的result()方法)。尽管任务池很容易处理
# 在设计大程序的时候还是有很多需要注意的地方，如下几点：
# * 这种并行处理技术只适用于哪些可以被分解为互相独立部分的问题。
# * 被提交的任务必须是简单函数形势。对于方法、闭包和其他类型的并行执行还不支持。
# * 函数参数和返回值必须兼容pickle，因为要使用进程间通信，所有解释器之间的交换数据必须被序列化
# * 被提交的任务函数不应保留状态或有副作用。除了打印日志之类简单的事情。

# 在Unix上进程池通过调用fork()系统调用被创建，
# 它会克隆Python解释器，包括fork时的所有程序状态。
# 而在Windows上，克隆解释器不会克隆状态。
# 实际的fork操作会在第一次调用pool.map()或pool.submit()后发生。
# 当混合使用进程池和多线程的时候要特别小心。
# 你应该在创建任何线程之前先创建并激活进程池（比如在程序启动的main线程中创建进程池）。

