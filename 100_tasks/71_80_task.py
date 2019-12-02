# Question 71
# Please write a program which accepts basic mathematic expression from console and print the
# evaluation result.
# Example:
# If the following string is given as input to the program:
# 35+3
# Then, the output of the program should be:
# 38
def calculator():
    expression = input('Enter basic mathematic expression: ')
    return eval(expression)
# print(calculator())

# Question 72
# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

def search_func(*args,item=None):
    item = int(input('Enter integer number for search: '))
    return [x for x,y in enumerate(sorted(list(*args))) if y == item]
# print(search_func([2,4,6,8,6.5]))

# Question 73
# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.
def search_func1(*args,item=None):
    item = int(input('Enter integer number for search: '))
    return [x for x,y in enumerate(sorted(list(*args))) if y == item]
# print(search_func1([2,4,6,8,6.5]))

# Question 74
# Please generate a random float where the value is between 10 and 100 using Python math module.

import random

def gen_random():
    return round(random.uniform(10,100),2)
# print(gen_random())

# Question 75
# Please generate a random float where the value is between 5 and 95 using Python math module.
    
import random

def gen_random1():
    return round(random.uniform(5,95),2)
# print(gen_random1())

# Question 76
# Please write a program to output a random even number between 0 and 10
# inclusive using random module and list comprehension.
import random

def even_random():
    return random.choice([x for x in range(0,11) if x%2==0])
# print(even_random())

# Question 77
# Please write a program to output a random number, which is divisible by 5 and 7,
# between 0 and 100 inclusive using random module and list comprehension.
#
import random

def random_5_7():
    return random.choice([x for x in range(0,101) if x%5==0 and x%7==0])
# print(random_5_7())

# Question 78
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
import random
def gen_rand_num():
    return random.sample(range(100,201),5)
# print(gen_rand_num())


# Question 79
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
import random
def even_rand_num():
    lst=[]
    while len(lst) <5:
        lst.append(random.choice([x for x in range(100,201) if x%2==0 and x not in lst]))
    return lst
# print(even_rand_num())

# Question 80
# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 ,
# between 1 and 1000 inclusive.
import random
def rand_num_1000():
    return random.sample([x for x in range(1,1000) if x%5==0 and  x%7==0],5)
# print(rand_num_1000())
