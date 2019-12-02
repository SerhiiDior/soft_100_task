lst = []
while True:
    s = input().split(',')
    if not s[0]:
        break
    lst.append(tuple(s))
lst.sort(key=lambda x:(x[0],x[1],x[2]))
print(lst)
