def even_number(a):
    if a%2==0:
        return True
    else:
        return False

tup1=(1,2,3,4,5,6,7,8,9,10)
lst=[]
for i in tup1:
    if even_number(i):
        lst.append(i)
tup2=tuple(lst)
print (tup2)
