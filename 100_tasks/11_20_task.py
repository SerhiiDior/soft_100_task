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
