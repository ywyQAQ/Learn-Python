# 构建了一个自定义容器对象，里面包含列表、元祖或其他可迭代对象。
# 你想直接在新容器对象上执行跌打操作。

# 实际上你只需要定义一个__iter__()方法，将迭代操作代理到容器内部的对象上去。比如：
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

# 在上面代码中， __iter__() 方法只是简单的将迭代请求传递给内部的 _children 属性。

# Python的迭代器协议需要__iter__()方法返回一个实现了__next__()方法的迭代器对象。
# iter(s)只是简单的通过调用s.__iter__()方法来返回对应的迭代器对象,就像len(s)会调用s.__len__()方法一样。
# __iter__()方法返回一个实现了__next__()方法的迭代器对象。