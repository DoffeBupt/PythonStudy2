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