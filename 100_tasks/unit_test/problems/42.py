def two_line_tuple(*t):
    return '{}\n{}'.format(t[:(int(len(t)/2))],t[-(int(len(t)/2)):])

print(two_line_tuple(1,2,3,4,5,6,7,8,9,10))