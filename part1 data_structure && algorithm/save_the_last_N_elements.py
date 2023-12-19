from collections import deque

def search(lines, pattern, history=5):
    """
    在写查询元素的代码时，通常会使用包含yield表达式的生成器函数，
    这样可以将搜索过程和使用所搜结果代码解耦。
    使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
    当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除。
    在队列两端插入或删除元素的时间复杂度都是O(1),区别与列表的O(n)。
    """
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

with open(r'../../cookbook/somefile.txt') as f:
    """
    保留最后n个元素。
    """
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-' * 20)

