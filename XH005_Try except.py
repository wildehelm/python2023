# *** 005_Try except ***
# 2023-02-24
# try except
# the try block contains code which might contain (cause) errors
# the except block is only exectued if an error occurs in the try block

try:
    eingabe = input('Enter a number:\n')
    zahl = int(eingabe)
    print('Thank you for the input')

except:
    print('Wrong input. Please try again later')
