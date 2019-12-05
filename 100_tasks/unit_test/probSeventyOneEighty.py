import math
import random
#71
def calculator(*args):
    expression = str(*args)
    return eval(expression)

#72
def task_72(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index

#73
def task_73(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index

#74
def task_74():
    return round((random.uniform(10.0, 100.0)),2)


#75
def task_75():
    return random.uniform(5.0, 95.0)

#76
def task_76():
    return [random.randrange(0, 10, 2)]

#77
def task_77():
    return random.choice([i for i in range(0, 11) if i % 5 == 0 and i % 7 == 0])

#78
def task_78():
    return random.sample(range(100, 201), 5)

#79
def task_79():
    return random.sample([i for i in range(100, 201) if i % 2 == 0], 5)
print(task_79())

#80
def task_80():
    return random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5)
