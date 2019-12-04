def range_2000_3001():
    return [x for x in range(2000,3001) if x%7==0 and x%5!=0 ]
# print(range_2000_3001())

def factor(num):
    if num == 1:
        return 1
    else:
        return num*factor(num-1)
print(factor(8))

def int_number(num):
    return {i:i*i for i in range(1,num+1)}
# print(int_number(4))


def generate_dict(n):
    return {i : i*i for i in range(1,n+1)}


def accept_seq(string):
    lst = [x for x in string.split(',') if x.isnumeric()]
    return lst,tuple(lst)
# print(accept_seq('34,67,55,33,12,98'))


def array_digit(x=3,y=5):
    lst = []
    for i in range(x):
        nested = []
        for j in range(y):
            nested.append(i*j)
        lst.append(nested)
    return lst
# print(array_digit())

def seq_of_word(*args):
    word = str(*args)
    return ','.join([x for x in sorted(word.split(','))])

# print(seq_of_word('without,hello,bag,world'))

def capitalize_word(word = 'Hello world'):
    return word.upper()

# print(capitalize_word())

def split_comma(*args):
    words=str(*args).split(' ')
    return ' '.join(sorted(set(([x for x in sorted(words)]))))
print(split_comma('Ukraine USA Spain Italy Ukraine USA Spain Italy'))

