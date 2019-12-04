def move_robot(*args, x=0, y=0):
    c = str( *args ).split( )
    for i in range(0, len(c)-1):


        if c[i] == 'UP':
            x -= int( c[i+1] )
        elif c[i] == 'DOWN':
            x += int( c[i+1] )
        elif c[i] == 'LEFT':
            y -= int( c[i+1] )
        elif c[i] == 'RIGHT':
            y += int(c[i+1])



    possition = round( (x ** 2 + y ** 2) ** 0.5 )
    return possition


# print(move_robot('RIGHT 2'))

def count_freq(*args):
    words =sorted(set(str(*args).split()))
    return [(i,words.count(i)) for i in words ]
    # res = for w in sorted(set(words)):
    #     print('{}:{}'.format(w,words.count(w)))

# print(count_freq("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"))


def square_val(n):
    return n*n


def doc_string(f):
    return f.__doc__
# print(doc_string(bank_account))
# print(doc_string(str))
# print(doc_string(super))


def sum(a,b):
    return a+b

def toString(a):
    return str(a)

def two_int_sum(*args):
    nums = list(str(*args).split())
    return int(nums[0]) + int(nums[1])

def union(a,b):
    return a+b