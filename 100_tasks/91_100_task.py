# Question 91
# By using list comprehension,
# please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
def only_index1(*args):
    return [e for i,e in enumerate(*args) if i not in (0,4,5)]
# print(only_index([12,24,35,70,88,120,155]))

# Question 92
# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
def only_index2(*args):
    return [e for e in list(*args) if e != 24]
# print(only_index2([12,24,35,70,88,120,155]))

# Question 93
# With two given lists [1,3,6,78,35,55]
# and [12,24,35,24,88,120,155], write a program to make a list whose elements are
# intersection of the above given lists.
def intersection_list():
    lst1 = set([1,3,6,78,35,55])
    lst2 = set([12,24,35,24,88,120,155])
    return set(set.intersection(lst1,lst2))
# print(intersection_list())

# Question 94
# With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.
def dublicat_lst(*args):
    lst = list(*args)
    for n in lst:
        if lst.count(n) > 1:
            lst.remove(n)
    return lst
# print(dublicat_lst([12,24,35,24,88,120,155,88,120,155]))

# Question 95
# Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:
    
    def __init__(self):
        pass
    
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"
    
male = Male()
famele = Female()
# print(male.getGender())
# print(famele.getGender())

# Question 96
# Please write a program which count and print the numbers of each character in a string input by console.
# Example:
# If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
from collections import Counter
def count_let():
    _str = 'abcdefgabc'
    lst = []
    for l in _str:
        lst.append(l.lower())
    return Counter(lst)
# print(count_let())

# Question 97
# Please write a program which accepts a string from console and print it in reverse order.
# Example:
# If the following string is given as input to the program:
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir

def rev_str(*args):
    return ''.join(reversed(str(*args)))
# print(rev_str('rise to vote sir'))

# Question 98
# Please write a program which accepts a string from console and print the characters that have even indexes.
# Example:
# If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld
def str_even_char():
    s = 'H1e2l3l4o5w6o7r8l9d'
    return ''.join([ s[i] for i in range(len(s)) if i%2 ==0 ])
# print(str_even_char())

# Question 99
# Please write a program which prints all permutations of [1,2,3]
def permut(*args):
    import itertools
    return list(itertools.permutations(list(*args)))
print(permut([1,2,3]))


# # Question 100
# # Write a program to solve a classic ancient Chinese puzzle: 
# # Cdef count_animals():
# def solve(numheads,numlegs):
#     ns='No solutions!'
#     for i in range(numheads+1):
#         j=numheads-i
#         if 2*i+4*j==numlegs:
#             return i,j
#     return ns,ns
# 
# numheads=35
# numlegs=94
# solutions=solve(numheads,numlegs)
# print(solutions)