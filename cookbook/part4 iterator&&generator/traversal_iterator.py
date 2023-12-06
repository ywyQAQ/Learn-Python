# 遍历一个可迭代对象中的所有元素，但是却不想使用for循环

# 为了手动的遍历可迭代对象，使用next()函数并在代码中捕获StopIteration异常。比如，
# 下面的例子手动读取一个文件中的所有行：

def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

# StopIteration用来指示迭代的结尾。然后，如果你手动使用上面演示的next()函数的话，
# 你还可以通过返回一个指定值来标记结尾，比如None。

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
    
# 大多数情况下，我们会使用for循环语句用来遍历一个可迭代对象。但是偶尔也需要对迭代做更加精确地控制，
# 这时候了解底层迭代机制显得尤为重要了。
