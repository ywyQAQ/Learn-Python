# 想定义一个生成器函数，但是它会调用某个暴露给用户使用的外部状态值。

# 如果你想让你的生成器暴露外部状态给用户，别忘了你可以简单的将它实现为一个类，然后把生成器函数
# 放到__iter__（）方法中过去。

from collections import deque

class linehistory:
    def __init__(self, lines, hislen=3) -> None:
        self.lines = lines
        self.history = deque(maxlen=hislen)
    
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    
    def clear(self):
        self.history.clear()

# 这个类可以当做一个普通的生成器函数。然而，由于可以创建一个实例对象，于是你可以
# 访问内部属性值，比如history属性或者是clear()方法。代码示例如下：
with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
    

# 关于生成器，很容易掉进函数无所不能的陷阱。如果生成器函数需要跟你的程序其他部分打交道的话
# （比如暴露属性值，允许通过方法来控制等等）。可能会导致代码异常复杂。如果是这种情况，
# 可以考虑使用上面介绍的定义类的方式，在__iter__()方法中定义你的生成器不会改变任何的算法逻辑。

# 一个注意的地方，如果迭代时不使用for循环语句，那么你得先调用iter()函数。比如：
f = open('somefile.txt')
lines = linehistory(f)
next(lines)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'linehistory' object is not an iterator

# Call iter() first, then start iterating
it = iter(lines)
next(it)
'hello world\n'
next(it)
'this is a test\n'
