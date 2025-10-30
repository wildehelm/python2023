# *** 0025_try while True zum Validieren.py ***
# 2023-02-24

print('Please enter a number: ')
while True:
    try:
        eingabe = int(input())
    except ValueError:
        print('Wrong input. Please use a number')
    else:
        break

print('The program may start. The input was', eingabe)