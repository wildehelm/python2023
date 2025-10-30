
# *** 035_Zuweisungsoperator ***

zahl = 23
print(zahl)

# multiple assignment in one command
# Die Zuweisung mehrerer Variablen in einer Anweisung
a, b = 'Apfel', 'Birne'
print(a)
print(b)
x = y = z = 1
print(x, y, z)      # 1 1 1
print((x, y, z) * 3)        # ! prints () as well, with 9 1s in between

# one-line swap
a, b = 'Apfel', 'Birne'
a, b = b, a                 # only to be found in Python
print(a, b)                 # Birne Apfel

# verkürzte Schreibweise des Zuweisungsoperators
# KEIN x++ in Python!
x = 0
x += 1      # same as x = x + 1
print(x)
x += 1
print(x)
x += 1
print(x)
# also valid: -=, *=, /=

# modulo: %
m = 7
m %= 3      # same as m = 7 % 3
print(m)    # 1

# **=
p = 2
p **= 5     # = 2 ^ 5 oder p = 2 ** 5
print(p)    # 32
print(2 ** 5)  # 32

# floor division: //=
i = 29
i //= 3         # oder
i = 29 // 3     # easier to read!
print(i)        # 9

