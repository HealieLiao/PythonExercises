"""
第1题：有一对兔子，从出生第三个月起每个月都生一对兔子，小兔子长到第三个月后，
每个月又生一对兔子，假如兔子都不死，问M个月时兔子的数量，M为键盘读入的正整数。
（这是一道面试题，请用python或者java语言作答）
"""

#实际上就是，求解斐波那契数列。我就用python来求解
#Fibonacci sequence：1,1,2,3,5,8,13,21,34......

def Fab(n):   #定义一个函数，用作计算斐波那契数列
    a1 = 1    #设置初始值
    a2 = 1
    a3 = 1
    if n < 1:
        print('input wrong')
        return -1
    while ( n - 2 ) > 0:
        a3 = a1 + a2    #将前两个数相加就是后面一个数
        a1 = a2
        a2 = a3
        n -= 1
    return a3

result = Fab(int(input('请输入月数：')))
if result != -1:
    print('总共有%d对小兔子诞生！'%result)

#lxl到此一游
