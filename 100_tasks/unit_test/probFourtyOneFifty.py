def tu(n):
    tup=tuple(i*i for i in range(1,n+1))
    return (tup)

def two_line_tuple(*t):
    return '{}\n{}'.format(t[:(int(len(t)/2))],t[-(int(len(t)/2)):])


def even_tuple():
    t = (1,2,3,4,5,6,7,8,9,10)
    return '{}'.format(tuple(filter((lambda x: x%2==0),t)))


def yes_no(*s):
    try:
        return '{}'.format((lambda x: 'Yes' if x=='yes' or x=='YES' or x=='Yes' \
                           else 'No')(*s))
    except ValueError:
        return 'Typing correct value'

def use_map_sq(*args):
    return list(map((lambda x: x**2),list(*args)))


