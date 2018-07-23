# http://bbs.fishc.org/thread-44821-1-1.html
# Q1:
def fun_A(x, y=3):
    return x * y

lambda x,y=3 : x*y

print(fun_A(1))

fun_B = lambda x , y=3 : x*y
print(fun_B(1))

# Q2:
lambda x : x if x % 2 else None

def fun_Q2(x):
    if x%2 == True:
        return x
    else:
        return None
# 有if的话，return前边，否则后边

# Q3：你可以利用filter()和lambda表达式快速求出100以内所有3的倍数吗？

list(filter(lambda x : not(x%3) , range(100)))
# not大法好hhh

# Q4:用列表推导式
list(x for x in range(100) if not(x%3))

# Q5:
list(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
ans = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# map 返回的是结果，后边依次丢进去的是各个参数的定义域
list(map(lambda x, y : [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
ans = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

# Q6：
def make_repeat(n):
    return lambda s: s * n


double = make_repeat(2)
print(double(8))
print(double('FishC'))

# 会返回16，fishcfishc
# 闭包，字符串成二等于重复两遍