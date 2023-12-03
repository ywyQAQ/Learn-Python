# 通过下标访问列表或者元组中元素的代码有时候会让你的代码难以阅读，
# 于是有时候想通过名称来访问元素。

# collections.namedtuple()函数通过使用一个普通的元组对象来帮你解决这个问题。
# 这个函数实际上是一个返回Python中标准元组类型子类的一个工厂方法。
# 需要传递一个类型名和你需要的字段给它，然后就会返回一个类，为你定义的字段传递值等。
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('phosssuki@gmail.com', '2001-03-10')
print(sub)
# Subscriber(addr='phosssuki@gmail.com', joined='2001-03-10')
print(sub.addr)
# phosssuki@gmail.com
print(sub.joined)
# 2001-03-10
print(len(sub))
# 2
addr, joined = sub
print(addr)
# phosssuki@gmail.com
print(joined)
# 2001-03-10

from collections import namedtuple
# namedtuple list
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
# 不像字典那样，一个命名元组是不可更改的。
# 如果你真的需要改变属性的值，那么可以使用命名元组实例的 _replace() 方法， 
# 它会创建一个全新的命名元组并将对应的字段用新的值取代。
s = s._replace(shares=75)
print(s)
# Stock(name='ACME', shares=75, price=123.45)

# _replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候， 
# 它是一个非常方便的填充数据的方法。 
# 你可以先创建一个包含缺省值的原型元组，
# 然后使用 _replace() 方法创建新的值被更新过的实例

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)
# Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
dict_to_stock(b)
# Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
