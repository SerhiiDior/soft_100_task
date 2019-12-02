class CustomException(Exception):
    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 0:
        raise CustomException("Input is less than 0")
    elif num > 0:
        raise CustomException("Input is grater than 0")
    elif num==0:
        raise CustomException("Input equal to 0")
except CustomException as custom:
    print("The error raised: " + custom.message)
