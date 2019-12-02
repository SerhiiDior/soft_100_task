import math
C=50
H=30
def MyLittleFunction(D):
    return math.sqrt((2*C*D)/H)
D=input("D=").split(',')
print(D)
D=[int(i) for i in D]
D=[MyLittleFunction(i) for i in D]
D=[round(i) for i in D]
print(D)
