# 反方向迭代一个实例

# 使用内置的reversed()函数，比如：
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# 反向迭代仅仅当对象的大小可预先确定或者对象实现了__reversed__()的特殊方法时
# 才能生效。如果两者都不符合，那你需要先把对象转换为一个列表才行，比如：

# Print a file backwards
f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')

# 如果可迭代对象很多的话，将其预先转换为一个列表要消耗大量的内存

# 很多程序员并不知道可以通过在自定义类上实现__reversed__()方法来实现反向迭代。
class Countdown:
    def __init__(self, start) -> None:
        self.start = start
    
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)

# 定义一个反向迭代器可以使得代码非常高效，因为不再需要把数据填充到一个列表中然后再反向迭代了。
