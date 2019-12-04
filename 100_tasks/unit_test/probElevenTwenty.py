
def four_digit_binary(*args):
    try:
        lst_num = [i for i in str(*args).split(',')]
        if len(lst_num) == 4:
            div_by_five = list(filter((lambda x: int(x,2) % 5 == 0), lst_num))
            return ' '.join(div_by_five)
    except:
        return 'Enter correct data or you typed more then 4 binary numbers!'
# print(four_digit_binary('0100,0011,1010,1001'))


def even_1000_3000():
    return (list(filter((lambda x: x%2==0),range(1000,3001))))
# print(even_1000_3000())


def letters_numbers(*args):
    sentence = str(*args)
    letters = [s for s in sentence if s.isalpha( )]
    num = [n for n in sentence if n.isnumeric( )]
    return ("LETTERS {}\nDIGITS {}".format( len( letters ), len( num ) ))

# print(letters_numbers('hello world! 123'))

def upper_lower(*args):
    sentence = str(*args)
    return ("UPPER CASE {}\nLOWER CASE {}".format(sum(map((str.isupper),sentence)),sum(map((str.islower),sentence))))

# print(upper_lower('Hello world!'))

def compute_value(a: str):
    b = int(a) + int(a + a) + int(a + a + a) + int(a + a + a + a)
    return b
# print(compute_value('9'))

def square_odd(*args):
    return list(filter((lambda x: x%2!=0),*args))
# print(square_odd([1,2,3,4,5,6,7,8,9]))

def sort_name_age(*args):
    lst = []
  # personal_data = input( 'Enter your name, age, height seperated by comma: ' )
    list_data = tuple(str(*args).split(','))
    lst.append( list_data )
    # if len(list_data) == 3 and list_data[0].isalpha and list_data[1].isnumeric and list_data[2].isnumeric:
    #     lst.append(list_data)
    # else:
    return sorted( lst, key=lambda x: (x[0], x[1], x[2]) )

# print(sort_name_age('John,23,90'))

