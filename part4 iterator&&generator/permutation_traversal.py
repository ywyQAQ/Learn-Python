# 迭代遍历一个集合中所有可能的排列或组合

# itertools模块提供了三个函数来解决这类问题。其中一个是itertools.permutations()，它接受一个集合并产生一个元组序列
# 每个元组由集合中所有元素的一个可能排列组成。

items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)

# 还可以指定长度的所有排列，可以传递一个可选的长度参数。
for p in permutations(items, 2):
    print(p)

# 使用itertools.combinations()可得到集合中元素的所有组合
from itertools import combinations
print('combinations')
for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

for c in combinations(items, 1):
    print(c)


# 函数itertools.combinations_with_replacement()允许同一个元素被选择多次，比如：
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
    