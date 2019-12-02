def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError:
    print("Dividing a number by zero!")
