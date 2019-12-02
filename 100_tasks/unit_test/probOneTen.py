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
print(accept_seq('34,67,55,33,12,98'))


# x,y = map(int,input("X,Y->").split(','))
def array_digit(x=3,y=5):
    return []


print(array_digit())