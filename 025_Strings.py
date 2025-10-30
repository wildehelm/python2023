
# *** String ***

print('Hello')          # Hello
print(type('Hello'))    # <class 'str'>

# indexing
# per eckigen Klammern
# sind null-basiert
s = 'Hello World'
print(s[0])     # H
print(s[6])     # W

# slicing
# Per Teilbereichsoperator
# der Anfang ist inklusiv und das Ende exklusiv
print(s[1:4])   # ell
print(s[0:4])   # Hell
print(s[:4])    # Hell
print(s[4:])    # o World (here the 4th character is included)

# negative indexing
print(s[-1])    # d
print(s[-5:-4])   # W
print(s[-5:])   # World (last 5 characters)

# Schrittweite
# Anfang:Ende:Schrittweite
s = 'Hello World'
print(s[1:11:3])    # eood
print(s[::2])       # HloWrd

# negative Schrittweite
# turns the sequence around
s = 'Hello World'
print(s[::-1])       # dlroW olleH

# ENDE muss immer größer als ANFANG sein!
print('Keine Ausgabe', s[4:0:1])        # 'Keine Ausgabe', but there is no warning
print('Keine Ausgabe', s[0:4:-1])       # 'Keine Ausgabe', but there is no warning
print('Keine Ausgabe', s[4::-1])        # olleH

# string operators - String-Operatoren: +, *
# + zum Verketten (concatenation)
x = 'Hello,'
y = 'World?'
z = x + ' ' + y
print(z)

# * seltener, aber in Python praktisch
# no need to build loops
print('Hello ' * 5)         # Hello Hello Hello Hello Hello
print('Hello ' * 2 * 2)     # Hello Hello Hello Hello

