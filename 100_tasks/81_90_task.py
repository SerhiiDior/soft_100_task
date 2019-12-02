# Question 81
# Please write a program to randomly print a integer number between 7 and 15 inclusive.
import random
def rand_num_7_15():
    return random.randrange(7,15)

# print(rand_num_7_15())

# Question 82
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
def compres_decom():
    import zlib
    string =zlib.compress(b"hello world!hello world!hello world!hello world!")
    decom_string = zlib.decompress(string)
    return '{}\n{}'.format(string,decom_string)
# print(compres_decom())

# Question 83
# Please write a program to print the running time of execution of "1+1" for 100 times.
def time_add():
    import time
    before = time.time()
    for i in range(100):
        x = 1 + 1
    after = time.time()
    execution_time = after - before
    return execution_time,
# print(time_add())

# Question 84
# Please write a program to shuffle and print the list [3,6,7,8].
def shuffl():
    import random
    lst = [3,6,7,8]
    random.shuffle(lst)
    return lst
# print(shuffl())

# Question 85
# Please write a program to shuffle and print the list [3,6,7,8].
def shuffl():
    import random
    lst = [3,6,7,8]
    random.shuffle(lst)
    return lst
# print(shuffl())

# Question 86
# Please write a program to generate all sentences where subject
# is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

def subject_gen():
    subjects,verbs,objects=["I", "You"],["Play", "Love"],["Hockey","Football"]
    lst = [[str(sub),str(ver),str(objec)] for sub in subjects for ver in verbs for objec in objects]
    return lst
# print(subject_gen())

  

# Question 87
# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
def delete_even(*args):
    return list(filter((lambda x: x%2!=0),*args))
# print(delete_even([5,6,77,45,22,12,24]))


# Question 88
# By using list comprehension,
# please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

def delete_div_by_7_5(*args):
    return list(filter((lambda x: x%5 !=0 and x%7 !=0),*args))
# print(delete_div_by_7_5([12,24,35,70,88,120,155]))

# Question 89
# By using list comprehension,
# please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
def only_index(*args):
    return [e for i,e in enumerate(*args) if i!=0 and i%2!=0]
# print(only_index([12,24,35,70,88,120,155]))

# Question 90
# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

def array_gen():
    return [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(array_gen())