def pow(a):
    return a**2

lst=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x: x % 2 == 0, lst))
res=list(map(pow,res))
print(res)
