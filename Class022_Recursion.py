# 例1 求阶乘
# 要点：
#   1.调用函数自身
#   2.正确的设置返回值
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1) # 到这里他就返回上一层开心的去寻找了
#
# number = int(input("输入一个正整数"))
# result = factorial(number)
# print("%d 的阶乘是 : %d " % ( number , result ))

# 递归的缺陷：
# 1.容易递归炸了
# 2.函数自己调用自己每次都要压栈弹栈保存回复寄存器blabla
# 3.递归用在恰到好处的地方最好，比如搞阶乘那个就不太合适

# def feibonaqie(n):
#     if n <= 2 :
#         return 1;
#     if n > 2:
#         return feibonaqie(n-1)+feibonaqie(n-2)
# for i in range(110):
#     print('第%d个斐波那契数列值为:%d'%(i+1,feibonaqie(i+1)))

def feibo1(n):
    n1 = 1
    n2 = 1
    n3 = 1 # 返回值

    while(n-2)>0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3

for i in range(110):
    print('第%d个斐波那契数列值为:%d'%(i+1,feibo1(i+1)))