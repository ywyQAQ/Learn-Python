# 想遍历一个可迭代对象，但是开始的某些元素并不感兴趣，想跳过它们。

# itertools模块中有一些函数可以完成这个任务。首先介绍的是itertools.dropwhile()函数。
# 使用时传递一个函数对象和一个可迭代对象。它会返回一个迭代器，丢弃原有序列中直到函数返回True之前的所有元素，然后返回后面的元素。

# 假定一个文件，开始前几行是注释。

from itertools import dropwhile

with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: not line.startswith('#'), f):
        print(line, end='')
    

# dropwhile()和islice()是两个帮助函数，为的是避免写出下面这种冗余代码：
with open('/etc/passwd') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)

# 本方案适用于所有可迭代对象。
