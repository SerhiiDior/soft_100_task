lst = []
for i in range(1000,3001):
    flag = 1
    for j in str(i):
        if ord(j)%2 != 0:
            flag = 0
    if flag == 1:
        lst.append(str(i))

print(",".join(lst))
