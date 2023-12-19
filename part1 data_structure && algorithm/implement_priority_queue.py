"""
实现一个优先队列
"""

import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        # 这个_index很有意思，是作为第二优先级的实现，保证优先级相同时保证顺序。
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        # 使用-1 拆出元组里面的item。
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
# Item('bar')
q.pop()
# Item('spam')
q.pop()
# Item('foo')
q.pop()
# Item('grok')
"""
仔细观察可以发现，第一个 pop()操作返回优先级最高的元素。 
另外注意到如果两个有着相同优先级的元素(foo和grok),
pop 操作按照它们被插入到队列的顺序返回的。
"""