# 有一系列排序序列，想把它们合并后得到一个排序序列并在上面迭代遍历。

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)

# heapq.merge可迭代特性意味着它不会立马读取所有序列。表示可以在很长的序列中使用
# 而不会有太大的开销。
with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)