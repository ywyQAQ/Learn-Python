# 现在有多个字典或者映射，你想在逻辑上将它合并为一个单一的映射后执行某些操作
# 比如查找值或者检查某些键是否存在

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 假设从两个字典中执行查找操作（比如先从a中找，然后再从b中找）。
# 一个简单的实现方法是collections模块中的ChainMap类。比如：
from collections import ChainMap
c = ChainMap(a, b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

# 一个ChainMap是从逻辑上变成了一个字典，并不是真的合并在一起，
# ChainMap类只是在内部创建了一个容纳这些自带你的列表，并重新定义了一些常见的字典操作来遍历这个列表。
print(len(c))
# 3
print(list(c.keys()))
# ['x', 'y', 'z']
print(list(c.values()))
# [1, 2, 3]

# 如果出现重复键，那么第一次出现的映射值会被返回。
# 对于字典的更新或删除操作总是影响的是列表中第一个字典。比如：
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
del c['y']
"""
Traceback (most recent call last):
...
KeyError: "Key not found in the first mapping: 'y'"
"""
# ChainMap 对于编程语言中的作用范围变量（比如 globals , locals 等）是非常有用的。
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
values
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values['x']
3
# Discard last mapping
values = values.parents
values['x']
2
# Discard last mapping
values = values.parents
values['x']
1
values
# ChainMap({'x': 1})

# 使用update()可以将两个字典合并，但这会创建一个完全不同的字典对象，或者破坏现有的字典结构。
# 或者原字典做了更新，这种改变不会反应到新的合并字典中去。
# ChainMap使用原来的字典，它自己不创建字典。所以它并不会产生上面的结果。
