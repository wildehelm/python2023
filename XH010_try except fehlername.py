# *** 010_try except fehlername.py ***
# 2023-02-24
# try except fehlername

# x = int('eins')       # ValueError:
# y = 100 / 0             # ZeroDivisionError

try:
    eingabe = input('Enter a number:\n')
    zahl = int(eingabe)
    ergebnis = 100 / zahl
    print('Thank you for the input:', ergebnis)

except ValueError:
    print('Wrong input. Please use a number')

except ZeroDivisionError:
    print('Please do not use a 0 (zero)')
