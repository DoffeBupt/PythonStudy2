# 被继承的类称为父类，基类，超类
# 儿子是子类
class Parent:
    def __init__(self):
        self.year = 40

    def hello(self):
        print('i am father, age is %s' % self.year)


class Son1(Parent):
    pass


# 继承后写同名内容的话会自动覆盖
# 注意是完全覆盖！原来方法的写的东西全部不见了
# 如果希望可以连方法也继承一波的话，可以用super或者是直接在子类调用父类
# 调用未绑定父类的方法
class Son2(Parent):
    def __init__(self):
        # 实际上可以理解为是调用了父类的方法来初始化了儿子
        # Parent.init(Son)
        Parent.__init__(self)

    def hello(self):
        print('i am son2')
        print('my father age is %s' % self.year)
class Son3(Parent):
    def __init__(self):
        super().__init__()
# 更牛逼的方法，直接用super，把祖宗家的属性都能给引入进来，一步到位
# 一般是多重继承用起来舒服
father = Parent()
son1 = Son1()
son2 = Son2()
father.hello()
son1.hello()
son2.hello()
# 多重继承：
class Base1:
    def foo1(self):
        print('woshiBase1,foo1')
class Base2:
    def foo2(self):
        print('woshiBase2,foo2')
class C(Base1,Base2):
    pass

# 多重继承尽量别用，容易出BUG，另外要是有重名的，会继承先编译的霸霸的