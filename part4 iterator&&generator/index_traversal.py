# 迭代一个序列的同时跟踪正在被处理的元素索引。

# 内置的enumerate()函数可以很好地解决这个问题：
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 还可以传递开始参数
for idx, val in enumerate(my_list, 1):
    print(idx, val)

# 在遍历文件想在错误消息中使用行号定位的时候非常有用：
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))
        

# 还可以跟踪某些值在列表中出现的位置。

word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

# 还有一点值得注意，有时候当你在一个已经解压后的元组序列上使用enumerate()函数时很容易调入陷阱。
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

# Correct!
for n, (x, y) in enumerate(data):
    ...
# Error!
for n, x, y in enumerate(data):
    ...
