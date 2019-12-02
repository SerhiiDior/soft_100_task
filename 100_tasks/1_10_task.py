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
def array_digit(x=3,y=5):
    lst = []
    for i in range(x):
        nested = []
        for j in range(y):
            nested.append(i*j)
        lst.append(nested)
    return lst


# 8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def seq_of_word():
    word = input('Comma separeated sequence of word: ')
    return ','.join([x for x in sorted(word.split(','))])
       
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
