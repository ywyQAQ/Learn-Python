# 封装实例私有数据，但是Python没有访问控制

# Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。
# 第一个约定是任何以下划线_开头的名字都应该是内部实现。比如：
class A:
    def __init__(self) -> None:
        self._internal = 0
        self.public = 1
    
    def public_method(self):
        pass

    def _internal_method(self):
        pass

# 还有可能会在类中定义使用两个下划线__开头的命名。比如：
class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()
    
# 使用双下划线开始会导致访问名称变成其他形势。比如，在前面的类B中，私有属性被分别重命名为
# _B__private 和　_B__private_method。你可能想问这样重命名的目的是什么？
# 答案就是集成——这种属性通过继承是无法被覆盖的。比如
class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private
    
    # Does not override B.__pricvate_method()
    def __private_method(self):
        pass

# 大部分情况下，以单下划线开头。但是，如果你清楚代码会涉及自雷，而且有些内部属性
# 应该在子类中隐藏起来，那么才考虑使用双下划线方案。
# 有时候定义的一个变量和一个保留关键字冲突，这时候可以使用单下划线作为后缀，例如：
lamada_ = 2.0