# Question 61
# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
def ascii_to_unicode():
    string = input('Enter ASCII string: ')
    unic = string.encode('utf-8')
    return unic
# print(ascii_to_unicode())

# Question 62
# Write a special comment to indicate a Python source code file is in unicode.
# -*- coding: utf-8 -*-

# Question 63
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.
def compute_sum():
    num = int(input('Enter number bigger then 0: '))
    return round(sum([i/(i+1) for i in range(1,num+1)]),2)
# print(compute_sum())

# Question 64
# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 500
# In case of input data being supplied to the question, it should be assumed to be a console input.
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100

# n = int(input('Typing int number: '))
# print(f(n))

# Question 65
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 13
# In case of input data being supplied to the question, it should be assumed to be a console input.

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
# print(fibo(n))

# Question 66
# The Fibonacci Sequence is computed based on the following formula:
# 
# 
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibo_2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibo_2(n-1) + fibo_2(n-2)
# print(fibo_2(300))


# Question 67
# Please write a program using list comprehension to print
# the Fibonacci Sequence in comma separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13

def fibo_3(n):
    a,b = 0,1
    while a < n:
        yield a
        a,b = b, a+b
        
solution = fibo_3(50)
# print(list(solution))

# Question 68
# Please write a program using generator to print the even numbers between 0 and n in comma
# separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10

def generator_even(n):
    return ','.join([(yield str(i)) for i in range(n+1) if i%2==0 ])
# print(generator_even(10))

# Question 69
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70

def div_by_5_7(n):
    return ','.join([(yield str(i)) for i in range(0,n+1) if i%5==0 and i%7==0])
# print(div_by_5_7(100))

# Question 70
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

def assert_stat(*args):
    for x in list(*args):
        assert x%2==0, "{} Not even".format(x)
# print(assert_stat([2,4,6,8]))