# *** 015_try except else.py ***
# 2023-02-24
# try except else - is executed if no errors occurred

# x = int('eins')       # ValueError:
# y = 100 / 0             # ZeroDivisionError

try:
    eingabe = input('Enter a number:\n')
    zahl = int(eingabe)
    ergebnis = 100 / zahl
    # this line could be seen as replacement of the else later down

except ValueError:
    print('Wrong input. Please use a number')

except ZeroDivisionError:
    print('Please do not use a 0 (zero)')
else:
    print('Thank you for the number:', ergebnis)

