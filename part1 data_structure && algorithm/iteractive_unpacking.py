from collections import deque

def drop_first_last(grades):
    """
    去除第一个和最后一个，获取中间所有的到middle.
    迭代解压语法。
    """
    first, *middle, last = grades
    return avg(middle)


"""
一种有意思的递归算法
"""

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head