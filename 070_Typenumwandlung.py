# *** 070_Typenumwandlung - type casting ***
# 2023-02-21
#################################################################
# explizite Umwandlung
#################################################################
# str(): verwandelt einen Wert in eine Textkette um
zahl = 42
# print('Die Antwort heißt ' + zahl)   # TypeError: can only concatenate str (not "int") to str
print('Die Antwort heißt '  + str(zahl))  # Die Antwort heißt 42
print(sorted('Die Antwort heißt '  + str(zahl)))    # play with sort: [' ', ' ', ' ', '2', '4', 'A', 'D', 'e', ...

# int(): verwandelt eine Textkette in einen Integer um
# zahl = input('Bitte eine Zahl eingeben! ')
zahl = '42'
print(type(zahl))  # <class 'str'>
# print(zahl + 7)  # TypeError: can only concatenate str (not "int") to str
print(int('9'))  # 9
print(int(zahl) + 7)  # 49
print(int(123.456))  # 123

print(int(True))    # 1     # in VBA True = -1!
print(int(False))    # 0

# float
print(float(123))           # 123.0
print(float('123.45'))      # 123.45
# dies hier geht nicht:
# print(int('123.45'))      # ValueError: invalid literal for int() with base 10: '123.45'
print(int(float('123.45')))   # 123

# bool()
print(bool('Hello'))        # True !
print(bool(''))             # False

#################################################################
# Impliziete Typenumwandlung
#################################################################
# booleans are changed to integers
print(True + True + False)      # 2
# Beispiel to check for passwort setup conditions
klein = True
gross = False
ziffern = True
sondern = True
if klein + gross + ziffern + sondern >= 3:
    print('Passwort ist gut genug')
else:
    print('Passwort muss verbessert werden')
