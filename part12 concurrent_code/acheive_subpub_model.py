# 你有一个基于线程通信的程序，想让它实现发布/订阅模式的消息通信。

# 要实现发布/订阅的消息通信模式，你通常要引入一个单独的交换机或网关对象作为所有消息的中介。
# 也就是说，不直接将消息从一个任务发送到另一个，而是发送到交换机，
# 然后由交换机将它发送给一个多多个被关联任务。下面是例子：

from collections import defaultdict

class Exchange:
    def __init__(self) -> None:
        self._subscribers = set()
    
    def attach(self, task):
        self._subscribers.add(task)
    
    def detach(self, task):
        self._subscribers.remove(task)
    
    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]

# 一个交换机就是一个普通对象，负责维护一个活跃的订阅者集合，并为绑定、解绑和
# 发送消息提供相应的方法。每个交换机通过一个名称定位，get_exchange()通过给定一个名称返回一个Exchange实例。
# 下面是一个简单例子，演示了如何使用一个交换机：

class Task:

    def send(self, msg):
        ...

task_a = Task()
task_b = Task()

# Example of getting an exchange
exc = get_exchange('name')

# Examples of subscribing tasks to it
exc.attach(task_a)
exc.attach(task_b)
# Example og unsubscribing
exc.detach(task_a)
exc.detach(task_b)

# 这个实现最重要的一个特点是它能兼容多个task-like对象。例如，消息接收者可以使actor
# 协程、网路连接或任何实现了正确的send()方法的东西。

# 解绑的正确实现
exc = get_exchange('name')
exc.attach(some_task)
try:
    ...
finally:
    exc.detach(some_task)

# 为了防止忘记最后的detach()步骤，为了简化这个，可以考虑使用上下文管理器协议。
# 在交换机上增加一个subscribe()方法
from contextlib import contextmanager

@contextmanager
def subsribe(self, *tasks):
    for task in tasks:
        self.attach(task)
    try:
        yield
    finally: 
        for task in tasks:
            self.detach(task)



# Example of using the subscribe() method

exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
    ...
    exc.send(msg1)
    exc.send(msg2)