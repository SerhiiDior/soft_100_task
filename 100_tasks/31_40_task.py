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
