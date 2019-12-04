def compare(a,b):
    if len(a)>len(b):
        return a
    elif len(a)<len(b):
        return b
    elif len(a)==len(b):
        return a+' '+b


def even_number(a):
    if a%2==0:
        return "It is an even number"
    else:
        return "It is an odd number"

def printdic():
    dic = {i: i * i for i in range(1,4)}
    return dic

def printkey(x):
    dic = {i: i * i for i in range(1,x+1)}
    return dic.keys()

def dict_value_2(a = 1, b = 6):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return list(map((lambda x: x),dictionary.values()))

def dict_value_3(a = 1, b = 20):
    dictionary = {x:x**2 for x in range(a,b+1)}
    return list(map((lambda x: x),dictionary.items()))[:5]