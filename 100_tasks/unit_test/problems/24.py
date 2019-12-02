print(abs.__doc__)
print(int.__doc__)

def even_number(a):
    '''
    a: This is any integer number.
    return: True if a is even number , False if a is odd number
    '''
    if a%2==0:
        return True
    else:
        return False

print(even_number(10))
print(even_number.__doc__)
