'''题目003：（华为）倒转字符串
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。例如：
'''

# -*- coding: utf-8 -*-
#python3.6.2,
#time: 2017.10.12

#第一种方法：简单的步长-1，即字符串的反转（较常用）

def reverse1(str):
    return str[::-1]

#第二种方法：交换前后字母的位置。注意：range中是字母L减去1，字母L整除2

def reverse2(str):
    t = list(str)
    L = len(t)
    for i,j in zip(range(L-1,0,-1),range(L//2)):
        t[i],t[j] = t[j],t[i]
    return "".join(t)

#第三种方法：递归。每次输出一个字符。

def reverse3(str):
    if len(str) <= 1:
        return str
    return reverse3(str[1:]) + str[0]

#第四种方法：双端队列，用extendleft()函数。

from collections import deque
def reverse4(str):
    d = deque()
    d.extendleft(str)
    return ''.join(d)

#第五种方法：for循环，从左至右输出。

def reverse5(str):
    #return ''.join(str[len(str)-i] for i in range(1, len(str)+1))
    return ''.join(str[i] for i in range(len(str)-1,-1,-1))


str = input()
print(reverse1(str))
print(reverse2(str))
print(reverse3(str))
print(reverse4(str))
print(reverse5(str))
