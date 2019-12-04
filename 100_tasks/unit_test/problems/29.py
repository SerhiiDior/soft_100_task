def sum_split(x):
    num1,num2 = map(int,x)
    return num1+num2

a=map(str,input("a b-->").split(' '))
a=sum(a)
print(a)
