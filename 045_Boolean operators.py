
# *** 045_Boolean operators - Boolsche Operatoren ***
# logical operators: and, or, not

# and or
print(True or True)         # True
print(False or True)        # True
print(False or False)       # False
print(2 > 1 or 6 == 7)      # True

# and
print('and True/False...')
print(True and True)        # True
print(False and True)       # False
print(False and False)      # False
print(2 > 1 and 6 == 7)     # False
print(3 > 2 and 7 != 8)     # True

# not / nicht
print('not True/False...')
print(not False)            # True
print(not True)             # False
print('not ==...')
x = 42
print(not (x == 23))        # True
print(not (42 == 23))       # True
