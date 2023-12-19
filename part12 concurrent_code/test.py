import random

def some_generator(data=1):
    result = yield data
    print(result)

# 使用这种形式的yield语句的函数通常被称为协程。通过调度器，yield语句在一个循环中被处理，如下：
f = some_generator(1)
# Initial result. Is None to start since nothing has been computed
result = None
while True:
    try:
        data = f.send(result)
        result = random.randint(1, 10000)
    except StopIteration:
        break