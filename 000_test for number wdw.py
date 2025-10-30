import math
stop = False
n = 0.0

while not stop:
    answ = input('Please enter the gross price: ')
    if not math.isnan(float(answ)):      # check to see if the input is numeric... it does not accept float
        n = float(answ)     # convert the answer into a float
        stop = True         # we are happy with the input
        print('Test4: input is a number!')
    else:
        print('Test4 failed. Input is not a number')
    if answ.isnumeric():
        print('Test1: input is numeric...')     # 4
    else:
        print('Test1 failed. Input is not numeric')
    if answ.isdigit():
        print('Test2: input is digit...')
    else:
        print('Test2 failed. Input is not digit')
    if answ.isdecimal():
        print('Test3: input is decimal')
    else:
        print('Test3 failed. Input is not decimal')