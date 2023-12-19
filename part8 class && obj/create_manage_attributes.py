# 给某个实例attribute增加除访问与修改之外的其他处理逻辑，不如类型检查或合法性验证。

# 自定义某个属性的一个简单方法就是将它定义为一个property。例如:增加了属性简单的类型检查：

class Person:
    def __init__(self, first_name) -> None:
        self._first_name = first_name
    
    # Getter function
    @property
    def first_name(self):
        return self._first_name
    
    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
    
    # Deleter function(optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
    
# 上述代码中有三个相关联的方法，这三个方法的名字都必须一样。
# 第一个方法是一个getter函数，它使得first_name成为一个属性。其他两个方法给first_name属性
# 添加了setter和deleter函数。需要强调的是只有在first_name属性被创建后，后面的两个装饰器
# @first_name.setter和@first_name.deleter才能被定义。

# property的一个关键特征是它看上去跟普通的attribute没什么两样，但是访问它的时候会自动触发
# getter、setter和deleter方法。

# 还能在已存在的get和set方法基础上定义property。例如：

class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)

    # 一个property属性其实就是一系列相关绑定方法的集合。如果你去查看拥有property的类，就会发现
    # property本身的fget、fset和fdel属性就是类里面的普通方法。比如：

Person.first_name.fget
# <function Person.first_name at 0x1006a60e0>
Person.first_name.fset
# <function Person.first_name at 0x1006a6170>
Person.first_name.fdel
# <function Person.first_name at 0x1006a62e0>

# 通常来说，你不会直接去调用fget或这fset，它们会在访问property的时候自动被触发。

# 只有确实需要对attribute执行额外的操作的时候才必须使用到property。有时候java过来的程序员
# 总认为所有的访问都应该通过getter和setter，他们认为代码应该像下面这样写：
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

# 不要这样做。
# Properties还是一种定义动态计算attribute的方法。这种类型的attributes并不会被实际的存储，
# 而是在需要的时候被计算出来。
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    

# 尽管properties可以实现优雅的编程接口，但有些时候你还是会想直接使用getter和setter函数。
p = Person('Guido')
p.get_first_name()
p.set_first_name('Larry')

# 这种情况的出现通常是因为Python代码被集成到一个大型基础平台架构或程序中。 
# 例如，有可能是一个Python类准备加入到一个基于远程过程调用的大型分布式系统中。 
# 这种情况下，直接使用get/set方法(普通方法调用)而不是property或许会更容易兼容。