# 对象 = 属性+方法
# 类的对象：实例化的对象
# 类名约定是以大写字母开头
# 类是为了量产对象的
# 面向对象 = OO object oriented
# python的列表就是一个对象==>所以经常有各种方法
# 封装：只是把方法和名字给了，具体实现不透露，相对更加安全
# 继承：子类自动复制父类的方法和参数
# 多态：不同类的对象的同一函数下有着不一一样的方法（同一个操作对于不同的对象会有着不一样的结果）
# 一般的形态是子类继承了父类，对父类的函数进行了重写，因而相同的名字有了不同的结果

# self是什么
# 当一个对象的方法被调用的时候，他自己就会被传入到self这个参数里

class Ball:
    def setName(self,name):
        self.name = name
        # ball.name
        # 默认name是第一个传入的参数
    def kick(self):
        print("我被踢了，我叫%s"%self.name)

a = Ball()
a.setName('球a')
b = Ball()
b.setName('球b')
c = Ball()
c.setName('土豆')
a.kick()
c.kick()

# init 构造函数，实例化对象的时候自动调用的东东
# 可以重写自定义初始化的操作

class Ball2(Ball):
    def __init__(self,name = '小西瓜'):
        self.name = name
d = Ball2('西瓜')
d.kick()
e = Ball2()
# 有括号才会悄悄地把self传入
e.kick()

# 私有属性、变量：外部不能直接通过a.xxx访问
# 而且还不让继承！！！
# 名字重整
# 伪装的私有，实际上是吧名字改成了_类名__变量名
class Person():
    __name = "doffe"
    age = 22
a = Person()
try:
    print(a.__name)
except:
    print('不让打印')
print(a._Person__name)
class PublicPerson():
    __name = 'doffe'
    def printname(self):
        print(self.__name)
b = PublicPerson()
b.printname()











