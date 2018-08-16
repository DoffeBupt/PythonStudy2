issubclass()
# 可以传入元组，看前边的人是不是后边的的儿子，此外，object类是所有人的霸霸
isinstance()
# 是否是类型
# 如果后边写的是他的霸霸，那么也依旧会说是ture
hasattr()
# 第一个是对象，第二个是属性名，问问对象有没有这个属性
getattr()
# 访问这个参数的值
setattr()
# 访问属性并且为之赋值，如果没有属性那么就建立属性
delattr()
# 删除指定的属性，不存在的话就抛出异常

property()
# 通过属性设置属性
# x = property(getSize,setSize,delSize)
# 直接访问a.x返回第一个，访问a.x=111调用第二个，访问del a.x调用第三个

