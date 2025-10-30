# *** 105_string methods ***

# 2023-02-22
# Test-Methoden die mit is- anfangen geben einen Boolean zurück
# Tipp
print((ord('A')))   # 65 ... see lower down


# islower()
print('asdfg'.islower())        # True
print('§(/&%§§$'.islower())     # False
print('asdFg'.islower())        # False
print('asdFg'.isupper())        # False
print('ASDFG'.isupper())        # True
print()


# isalpha: tests if all are letters
print('Test isalpha')
print('TTT'.isalpha())      # True
print('123TTT'.isalpha())    # False
print()


# isalnum: tests if all are letters OR numbers
print('Test isalnum')
print('TTT'.isalnum())      # True
print('123TTT'.isalnum())    # True
print()


# Funktion, die von einem Zeichen den ASCII zurückgibt
print('ASCII order number')
print(ord('A'))         # 65
print()


# change case to UPPER or lower
print('UPPER and lower')
print('abcdef'.upper())     # ABCDEF
print(('HELLO'.lower()))    # hello
print()


# make first letter capital
print('Capitalize')
print('hello world'.capitalize())   # Hello world
print()


# join()
# Gewöhnungsbedürftig (überall anders / andersrum)
# would have been (elsewhere) print(s.join('-'))
print('join function')
s = 'abcdefghijklm'
print('-'.join(s))  # a-b-c-d-e-f-g-h-i-j-k-l-m
print('-'.join(['Peter', 'Paul', 'Mary']))  # Peter-Paul-Mary
print()


# split
# the standard separator is a single space
print('split function')
print('Paul findet Python toll'.split())    # ['Paul', 'findet', 'Python', 'toll']

print(sorted('Paul findet Python toll'.split()))    # ['Paul', 'Python', 'findet', 'toll'] just for fun
print()


# strip([s]) - to trim
# s ist standardmäßig das Leerzeichen
print('strip function')
print('-' + 'Hello   '.strip() + '-')   # -Hello-
print()


# replace(old, new)
print('replace function - is not destructive (the original stays unchanged)')
s = 'abcdefghijklabcm'
print(s.replace('abc', '___'))
print(s)
s = s.replace('abc', '___')  # this changes the string
print(s)
print()


# refer to pop 060 Listen
