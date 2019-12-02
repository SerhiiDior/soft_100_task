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