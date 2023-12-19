# 一般是重新定义__str__()和__repr__()方法。

# __repr__()方法返回一个实例的代码表示形式，通常用来重新构造这个实例。
# __str__()转换为一个字符串。

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
    

# 特别来说，!r格式化代码指明输出使用__repr__()来代替默认的__str__()。
# __repr__()生成的文本字符串标准做法是让eval(repr(x)) == x为真。如果不能这样，
# 也应该创建一个有用的文本表示，并使用<>括起来。

# 如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。

# 上面的 format() 方法的使用看上去很有趣，格式化代码 {0.x} 对应的是第1个参数的x属性。 
# 因此，在下面的函数中，0实际上指的就是 self 本身：
def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)
# 作为这种实现的一个替代，你也可以使用 % 操作符，就像下面这样：
def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)