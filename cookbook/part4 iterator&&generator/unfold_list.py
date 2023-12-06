# 将一个多层嵌套的序列展开成一个单层列表

# 可以使用yield from语句的递归生成器来轻松解决这个问题。比如：

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

# 在上面代码中，isinstance(x, Iterable)检查某个元素是否是可迭代的。
# 如果是的话，yield from就会返回所有子例程的值。最终返回结果就是一个没有嵌套的简单序列了。

# 额外的参数ignore_types和检测语句isinstance(x, ignore_types)用来将字符串和字节排除在可迭代
# 对象之外，防止将它们再展开成单个字符。这样的话字符串数组就能最终返回我们期望的结果了。

# yield from在你想在生成器中调用其他生成器作为子例程的时候非常有用。但是你不使用它的话，
# 那么就必须写额外的for循环了。比如：

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x
