def bank_account():
    total = 0
    while True:
        s = input().split()
        if not s:
            break
        cm,num = map(str,s)

        if cm=='D':
            total+=int(num)
        if cm=='W':
            total-=int(num)
    return total
