# 想通过format()函数和字符串方法使得一个对象能支持自定义的格式化

# 为了自定义的格式化，我们需要在类上定义__format__()方法。例如

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}' 
}

class Date:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, __format_spec: str) -> str:
        if __format_spec == '':
            __format_spec = 'ymd'
        fmt = _formats[__format_spec]
        return fmt.format(d=self)

# 现在Date类支持格式化操作了，如同下面这样
d = Date(2012, 12, 21)
print(format(d))
print(format(d, 'mdy'))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))

# __format__()方法给Python的字符串格式化功能提供了一个钩子。
# 格式化代码的解析工作完全由类自己决定。
# 因此格式化diamante可以是任何值。
