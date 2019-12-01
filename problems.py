# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def div_by_seven():
    return '{}'.format(','.join([str(x) for x in range(2000,3201) if x%7==0 and x%5!=0]))
# print(div_by_seven())

# 2. Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def factor(num):
    if num == 1:
        return 1
    else:
        return num*factor(num-1)
#print(factor(8))
    
# 3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def int_number():
    try:
        num = int(input('Enter number: '))
        return {i:i*i for i in range(1,num+1)}
    except:
        return 'Enter valid data'
#print(int_number())
    
# 4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
def accept_seq():
    try:
        seq = input('Enter sequence of comma-separated: ')
        lst = [x for x in seq.split(',') if x.isnumeric()]
        return lst, tuple(lst)
    except:
        return -1
# print(accept_seq())

# 5. Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class SimpleString:
    
    def getString(self):
        self.string1 = str(input())
    
    def printString(self):
        print(self.string1.upper())
    
# str1 =SimpleString()
# str1.getString()
# str1.printString()
#

# 6. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# def square_root():
#    
#     d = input('Enter sequence of comma-separated: ')
#     c = 50
#     h = 30
#    
#     return [0.5**((2*c*int(x))/h) for x in d.split(',') if x.isnumeric()]
    
# print(square_root())

# 7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,ВЎВ­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


# 8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def seq_of_word():
    word = input('Comma separeated sequence of word: ')
    for x in sorted(word.split(',')):
        print(x, end=',')
# print(seq_of_word())


# 9. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def sep_lines():
    lst_seq = []
    while True:
        lines = input("Enter sequence of lines, if enter 'q' will be exit: ")
        if lines != 'q':
            lst_seq.append(lines)
        else:
            return str(lst_seq).upper()
#print(sep_lines())
        
# 10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def whitspace_sep():
    try:
        word = input('Whitespace separeated word: ')
        return str(sorted(set(([x for x in sorted(word.split())]))))
    except:
        return 'Input correct data'
# print(whitspace_sep())

# 11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

def four_digit_binary():
    try:
        numbers = input('comma separated 4 digit binary numbers')
        div_by_five = [i for i in numbers.split(',') if int(i,2)%5==0 ]
        return div_by_five
    except:
        return 'Enter correct data'
# print(four_digit_binary())

# Question 12
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def even_1000_3000():
    return list(filter((lambda x: x%2==0),range(1000,3001)))
# print(even_1000_3000())

# Question 13
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def letters_numbers():
    sentence = input("Write the sentence with letters and numbers: ")
    letters = [s for s in sentence if s.isalpha()]
    num = [n for n in sentence if n.isnumeric()]
    print("LETTERS {} \n\rDIGITS {}".format(len(letters),len(num)))
    return ''
# print(letters_numbers())

# Question 14
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def upper_lower():
    sentence = input("Write the sentence with letters and numbers: ")
    print("UPPER CASE {} \n\rLOWER CASE {}".format(sum(map((str.isupper),sentence)),sum(map((str.islower),sentence))))
    return ''
# print(upper_lower())

# Question 15
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
def comp_value_a(a):
    print(eval('{0}+{0}{0}+{0}{0}{0}+{0}{0}{0}{0}'.format(a)))
    return ''
# print(comp_value_a(9))

# Question 16
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

def square_odd(*args):
    return list(filter((lambda x: x%2!=0),*args))
# print(square_odd([1,2,3,4,5,6,7,8,9]))


# Question 17
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

def bank_account():
    """a program that computes the net amount of a bank account based a transaction log from console input
        
       Parameter: D & sum  - deposit
       Parameter: W & sum  - withdrawal
       Return: summary on bank account after ended operrations with added deposit and withdrawal money from deposit 
    """
    deposit = 0
    print("For exit press 'Enter'")
    try:
        while True:
            chose = input("Enter D(for deposit) or W(witgdraw) and sum separate whitespaces: ")
            if chose != 'q':
                operation_sum = [x for x in chose.split()]
                
                if len(operation_sum) == 2:
                    if operation_sum[0] == "D":
                        deposit += int(operation_sum[1])
                    elif operation_sum[0] == "W":
                        if (deposit - int(operation_sum[1])) < 0: # check if after withdraw balnce not be negetive
                            print('You have not enoght money')
                        else:
                            deposit -= int(operation_sum[1])
                else:
                    return 'Your balnce is {}'.format(deposit)
    except:
        return 'Enter correct data'
        
# print(bank_account())


# Question 18
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# def valid_password():
#     import re
#     password = input('Enter your password: ')
#     reg = '[A-Za-z0-9$#@]{6,12}'
#     compiling  = re.compile(reg)
#     check = re.search(compiling,password)
#     return list(filter((lambda p: re.match(p,check)), password.split(',')))
# print(valid_password())
#


# Question 19
# You are required to write a program to sort the (name, age, height)
# tuples by ascending order where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

def sort_name_age():
    lst = []
    while True:
        print('For exit press ENTER')
        personal_data = input('Enter your name, age, height seperated by comma: ')
        list_data = tuple(personal_data.split(','))
        if len(list_data) == 3 and list_data[0].isalpha and list_data[1].isnumeric and list_data[2].isnumeric:
            lst.append(list_data)
        else:
            return sorted(lst,key = lambda x: (x[0],x[1],x[2]))
        
# print(sort_name_age())

# Question 20
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.


class DivisibleBySeven:
    
    def __init__(self):
        self.n = int(input('Enter number: '))
    
    def generator(self):
        return [i for i in range(self.n+1) if i%7==0]  

number = DivisibleBySeven()
# print(number.generator())


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

def move_robot(x = 0, y = 0):
    try:
        while True:
            print('For exit just press "ENTER"')
            c = input('''Please typing direction seperated by whitespace
"UP, DOWN, LEFT and RIGHT" and amount of steps:  ''').split()
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
# print(move_robot())


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

def square_val():
    num = input('Enter number: ')
    if isinstance(float(num),float):
        return round((float(num)**2),2)
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

# Question 31
# Define a function that can accept two strings
# as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line.
def compare_two_line():
    f_line = input("Enter first line: ")
    s_line = input("Enter second line: ")
    if len(f_line) == len(s_line):
        return '{} {}'.format(f_line,s_line)
    return (lambda x,y: x if (len(x) > len(y)) else y)(f_line,s_line)
# print(compare_two_line())

# Question 32
# Define a function that can accept an integer number as input and print the
# "It is an even number" if the number is even, otherwise print "It is an odd number".
def even_or_odd(a: int):
    try:
        return (lambda x: "It is an even number" if x%2==0 else "It is an odd number")(a)
    except ValueError:
        return 'Enter integer value!!!'
# print(even_or_odd(7))

# Question 33
# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.
def dict_square(a = 1, b = 3):
    return {x:x**2 for x in range(a,b+1)}
# print(dict_square())

# Question 34
# Define a function which can print a dictionary
# where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.
def dict_square_twenty(a = 1, b = 20):
    return {x:x**2 for x in range(a,b+1)}
# print(dict_square_twenty())

# Question 35
# Define a function which can generate a dictionary
# where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the values only.
def dict_value(a = 1, b = 20):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return '{}'.format(dictionary.values())
# print(dict_value())

# Question 36
# Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included)
# and the values are square of keys.
# The function should just print the keys only.
def dict_value(a = 1, b = 20):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return '{}'.format(dictionary.values())
# print(dict_value_1())

# Question 37
# Define a function which can generate and print a list
# where the values are square of numbers
# between 1 and 20 (both included).
def dict_value_2(a = 1, b = 20):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return list(map((lambda x: x),dictionary.values()))
# print(dict_value_2())

# Question 38
# Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.
def dict_value_3(a = 1, b = 20):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return list(map((lambda x: x),dictionary.items()))[:5]
# print(dict_value_3())

# Question 39
# Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.
def dict_value_4(a = 1, b = 20):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return list(map((lambda x: x),dictionary.items()))[-5:]
# print(dict_value_4())

# Question 40
# Define a function which can generate a list where the values are square
# of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.

def dict_value_5(a = 1, b = 20):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return list(map((lambda x: x),dictionary.values()))[:5]
# print(dict_value_5())

# Question 41
# Define a function which can generate and print a tuple
# where the value are square of numbers between 1 and 20 (both included).
def tuple_value(a = 1, b = 20):
    return tuple(map((lambda x: x**2),range(a,b+1)))
# print(tuple_value())

# Question 42
# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values in one line and the last half values in one line.
def two_line_tuple(*t):
    return '{}\n{}'.format(t[:(int(len(t)/2))],t[-(int(len(t)/2)):])
# print(two_line_tuple(1,2,3,4,5,6,7,8,9,10))

# Question 43
# Write a program to generate
# and print another tuple whose values are even numbers
# in the given tuple (1,2,3,4,5,6,7,8,9,10).
def even_tuple(*t):
    return '{}'.format(tuple(filter((lambda x: x%2==0),*t)))
# print(even_tuple((1,2,3,4,5,6,7,8,9,10)))

# Question 44
# Write a program which accepts a string
# as input to print "Yes" if the string is
# "yes" or "YES" or "Yes", otherwise print "No".
def yes_no(*s):
    try:
        return '{}'.format((lambda x: 'Yes' if x=='yes' or x=='YES' or x=='Yes' \
                           else 'No')(*s))
    except ValueError:
        return 'Typing correct value'
# print(yes_no('jdk'))

# Question 45
# Write a program which
# can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

def use_filter_even(*args):
    return list(filter((lambda x: x%2==0),*args))
# print(use_filter_even([1,2,3,4,5,6,7,8,9,10]))

# Question 46
# Write a program which can map()
# to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

def use_map_sq(*args):
    return list(map((lambda x: x**2),*args))
# print(use_map_sq([1,2,3,4,5,6,7,8,9,10]))

# Question 47
# Write a program which can map() and filter()
# to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
def map_filter(*args):
    return list(map((lambda x: x**2),filter((lambda x: x%2==0),*args)))
# print(map_filter([1,2,3,4,5,6,7,8,9,10]))

# Question 48
# Write a program which can filter()
# to make a list whose elements are even number between 1 and 20 (both included).
def filter_even():
    return list(filter((lambda x: x%2==0),range(1,21)))
# print(filter_even())

# Question 49
# Write a program which can map()
# to make a list whose elements are square of numbers between 1 and 20 (both included).
def map_square():
    return list(map((lambda x: x**2),range(1,21)))
# print(map_square())

# Question 50
# Define a class named American which has a static method called printNationality.
class American:
    
    @staticmethod
    def printNationality():
        return 'I am Arerican'
        
nationality = American()
# print(nationality.printNationality(),American.printNationality())

# Question 51
# Define a class named American and its subclass NewYorker.
class American:
    
    def __init__(self,nationality='USA'):
        self.nationality = nationality
        
    def printNationality(self):
        return self.nationality
    
    def __repr__(self):
        return self.nationality
    
class NewYorker(American):
    pass

person1 = American()
person2 = NewYorker()
# print(person1, person2)
    
# Question 52
# Define a class named
# Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
class Circle:
    
    def __init__(self, radius,pi=3.14):
        self.radius = radius
        self.pi = pi
        
    def calculate(self):
        return round((self.radius**2 * self.pi),2)
    
area = Circle(7)
# print(area.calculate())

# Question 53
# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle:
    
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
        
    def compute(self):
        return self.lenght * self.width
area = Rectangle(3,5)
# print(area.compute())


# Question 54
# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    
    def __init__(self):
        pass 
    
    def area(self):
        return 0
    
class Square(Shape):
    
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length
        
        
        
    def area(self):
        return self.length*self.length
    
solution = Square(6)
# print(solution.area())
# print(Square().area())

# Question 55
# Write a function to compute 5/0 and use try/except to catch the exceptions.

def Division_Zero(n=0):
    try:
        return 5/n
    except ZeroDivisionError as err:
        return 'division by zero is undefined'
# print(Division_Zero())

# Question 56
# Define a custom exception class which takes a string message as attribute.

class CustomException(Exception):
    
    def __init__(self,message):
        self.message = message

error = CustomException('reboot...')


# Question 57
# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# In case of input data being supplied to the question, it should be assumed to be a console input.

def name_from_email(email):
    try:
        return '{}'.format("".join([x for x in email.split('@')[0] if x.isalpha()]) )
    except:
        return 'Enter correct email: first part before @ must be alphabetical symbols!'

# print(name_from_email('John@gmail.com'))

# Question 58
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# google
# In case of input data being supplied to the question, it should be assumed to be a console input.


def email_from_email(email):
    import re
    pattern = "\w+@(\w+).com"
    mail = re.findall(pattern,email)
    return ''.join(mail)
# print(email_from_email('John@google.com'))

# Question 59
# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
# Example:
# If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

def output_digit(*args):
    return list(filter((lambda x: x.isnumeric()),*args))
# print(output_digit('2 cats and 3 dogs.'))

# Question 60
# Print a unicode string "hello world".

def printUnicode(string = 'hello world'):
    return u'{}'.format(string)
# print(printUnicode())

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

n = int(input('Typing int number: '))
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
print(fibo(n))


            
        
    
    















    













    
            
        
        
    

    



