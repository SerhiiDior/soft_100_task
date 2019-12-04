# Question 21
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ВЎВ­
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position
# after a sequence of movement and original point. If the distance is a float,
# then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

def move_robot(* args, x = 0, y = 0):
    try:
        while True:
            print('For exit just press "ENTER"')
            c = str(*args).split()
            if not c:
                break
            else:
                if c[0] == 'UP':
                    x -=int(c[1])
                if c[0] == 'DOWN':
                    x +=int(c[1])
                if c[0] == 'LEFT':
                    y -=int(c[1])
                if c[0] == 'RIGHT':
                    y +=int(c[1])
            
        possition = round((x**2 + y**2)**0.5)
        return possition
    
    except Exception:
        return 'You make a mistake please, reboot program'
# print(move_robot("UP 5 DOWN 3 LEFT 3 RIGHT 2"))


# Question 22
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

def count_freq():
    words = input().split()
    for w in sorted(set(words)):
        print('{}:{}'.format(w,words.count(w)))
        
        
# print(count_freq())

# Question 23
# Write a method which can calculate square value of number

def square_val(n):
    if isinstance(float(n),float):
        return round((float(n)**2),2)
    else:
        return 'Enter correct data'
# print(square_val())

#import bank_account

def doc_string(f):
    return f.__doc__
# print(doc_string(bank_account))
# print(doc_string(str))
# print(doc_string(super))


# Question 25
# Define a class, which have a class parameter and have a same instance parameter.

class ParametrClass:
    
    name = 'John'
    age = 43
    
    
    def __init__(self,name=None, age=None ):
        self.name = name
        self.age = age
  
    
    def __repr__(self):
        return '{},{}'.format(self.name, self.age)
        
person = ParametrClass()
# print(person)

person1 = ParametrClass()
person1.name = 'Will'
person1.age = 34
# print(person1)

person2 = ParametrClass('Bob', 23)
# print(ParametrClass.name, person2.name, person2.age)

# Question 26
# Define a function which can compute the sum of two numbers.

def sum_two():
    a,b = input('Enter two numbers seperate by whitespace: ').split()
    return float(a)+float(b)
# print(sum_two())

# Question 27
# Define a function that can convert a integer into a string and print it in console.

def int_to_str():
    try:
        integer = int(input("Enter integer number: "))
        covert_to_str = lambda x: str(x)
        number = covert_to_str(integer)
        return number, type(number)
    except ValueError:
        return 'Not valid number'
# print(int_to_str())
# 
# Question 28
# Define a function that can convert a integer into a string and print it in console

def int_to_str():
    try:
        integer = int(input("Enter integer number: "))
        covert_to_str = lambda x: str(x)
        number = covert_to_str(integer)
        return number, type(number)
    except ValueError:
        return 'Not valid number'
# print(int_to_str())

# Question 29
# Define a function that can receive two integral
# numbers in string form and compute their sum and then print it in console.

def two_int_sum():
    nums = list(input().split())
    return int(nums[0]) + int(nums[1])
# print(two_int_sum())

# Question 30
# Define a function that can accept two strings as input and concatenate them and then print it in console.
def concat_two_line():
    first_line = input("Enter first line: ")
    second_line = input("Enter second line: ")
    return '{} {}'.format(first_line,second_line)
# print(concat_two_line())