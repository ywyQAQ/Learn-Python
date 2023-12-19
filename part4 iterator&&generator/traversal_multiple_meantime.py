# 同时迭代多个序列，每次分别从一个序列中取一个元素、

# 为了同时迭代多个序列，使用zip()函数。

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
    print(x, y)

# 会返回一个(x,y)的迭代器，一旦一个序列到底结尾，迭代停止。

# 也可以使用itertools.zip_longest函数来替代。
from itertools import zip_longest

for i in zip_longest(a, b):
    print(i)

# 现在迭代出的是None，可以自己指定填充字符。

for i in zip_longest(a, b, fillvalue=0):
    print(i)


# 和dict使用有奇效。
# zip可以接受多于两个的序列的参数，zip返回的是生成器。
