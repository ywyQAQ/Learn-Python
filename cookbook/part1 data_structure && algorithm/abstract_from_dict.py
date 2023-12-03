# 想构造一个字典，它是另外一个字典的子集。
# 最简单的方式就是使用字典推导
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

# 大多数情况下字典推导能做到的,通过创建一个元组序列然后把它传给dict()函数也能实现。
p1 = dict((key, value) for key, value in prices.items() if value > 200)
# 但是，字典推导方式表意更清晰，并且实际上也会运行的更快些 
#（在这个例子中，实际测试几乎比 dict() 函数方式快整整一倍）。
