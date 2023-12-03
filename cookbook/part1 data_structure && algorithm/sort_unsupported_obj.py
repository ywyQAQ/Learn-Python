# 内置的sorted()对象有一个关键字参数key, 这个callable对象对每个传入的对象返回一个值。
# 这个值用来排序这些对象。比如，可以通过user_id值的来比较。
class User:
    def __init__(self, user_id) -> None:
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

# 另一种方法是使用operator.attrgetter()来代替lambda函数：
users = [User(23), User(3), User(99)]

from operator import attrgetter
sorted(users, attrgetter('user_id'))
# [User(3), User(23), User(99)]