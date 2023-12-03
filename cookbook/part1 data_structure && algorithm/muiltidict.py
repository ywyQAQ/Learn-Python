# 如何实现一个键对应多个值的字典？ multidict
# 解决方案：
# 一个键对应的多个值放入另外的容器中，比如列表或者集合里面。

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict

"""
你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。 
defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，
所以你只需要关注添加元素操作了。比如：
"""

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)


# 一般来讲，创建一个多值映射字典是很简单的。
# 但是，如果你选择自己实现的话，那么对于值的初始化可能会有点麻烦， 
# 你可能会像下面这样来实现：

d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
    
# 如果使用 defaultdict 的话代码就更加简洁了：

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)