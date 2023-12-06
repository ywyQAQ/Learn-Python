# 对多个对象执行相同的操作，但是这些对象在不同的容器中。

# itertools.train()方法可以用来简化这个任务。它接受一个可迭代对象作为输入，
# 并返回一个迭代器，有效的屏蔽掉多个容器中迭代细节。

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

# 使用chain()的一个常见场景是当你想对所有元素执行某些操作的时候。
active_items = set()
inactive_items = set()

for item in chain(active_items, inactive_items):
    # Process item
    ...
