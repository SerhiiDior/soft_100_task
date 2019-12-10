from math import pi
class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return pi*(self.radius**2)

r=float(12)
circle=Circle(r)


def divide_by_zero():
    try:
        5 / 0
    except ZeroDivisionError:
        print( "Dividing a number by zero!" )



def valid_email(*args):
    email=str(*args)
    email= email.split('@')
    return email[0]


def email_from_email(*args):
    import re
    email = str(*args)
    pattern = "\w+@(\w+).com"
    mail = re.findall(pattern,email)
    return ''.join(mail)


def output_digit(*args):
    return list(filter((lambda x: x.isnumeric()),*args))



