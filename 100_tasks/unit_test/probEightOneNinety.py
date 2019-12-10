import random
import zlib
from timeit import Timer
#81
def task_81():
    return random.randint(7,15)

#82
def task_82():
    s = 'hello world!hello world!hello world!hello world!'.encode()
    k = zlib.compress(s)
    return k,zlib.decompress(k)
print(task_82())
#83
def task_83():
    t = Timer("for i in range(0,101):1+1")
    return t.timeit()

#84
def task_84():
    lst=[3,6,7,8]
    return random.shuffle(lst)

#85
def task_85():
    lst=[3,6,7,8]
    return random.shuffle(lst)

#86
def task_86():
    for i in ["I", "You"]:
        for j in ["Play", "Love"]:
            for k in ["Hockey", "Football"]:
                return(i + " " + j + " " + k)

#87
def task_87():
    lst = [5, 6, 77, 45, 22, 12, 24]
    for i in lst:
        if i%2==0:
            lst.remove(i)
    return lst

#88
def task_88():
    lst = [12,24,35,70,88,120,155]
    for i in lst:
        if i%5==0 and i%7==0:
            lst.remove(i)
    return lst
#89
def task_89():
    lst = [12,24,35,70,88,120,155]
    lst.remove(lst[0])
    lst.remove(lst[2])
    lst.remove(lst[4])
    lst.remove(lst[6])
    return lst

#90
def task_90():
    return [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
