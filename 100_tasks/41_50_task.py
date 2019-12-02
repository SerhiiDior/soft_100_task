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