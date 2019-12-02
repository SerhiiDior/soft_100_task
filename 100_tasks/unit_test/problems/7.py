x,y = map(int,input("X,Y->").split(','))
a = [[0] * x] * y
for i in range(len(a)):
    print("\n")
    for j in range(len(a[i])):
        a[i][j]=i*j
        print("{:4d}".format(a[i][j]),end='')
