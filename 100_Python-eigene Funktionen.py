# *** 100_Python-eigene Funktionen ***

# built-in functions

builtins = dir(__builtins__)
print(builtins)

c = 0
for i in builtins:
    if i[0].islower():
        print(i, end=' ')
        c += 1
        if c % 17 == 0:
            print()
print()
'''abs aiter all anext any ascii bin bool breakpoint bytearray bytes callable chr classmethod compile complex copyright 
credits delattr dict dir divmod enumerate eval exec exit filter float format frozenset getattr globals hasattr hash 
help hex id input int isinstance issubclass iter len license list locals map max memoryview min next 
object oct open ord pow print property quit range repr reversed round set setattr slice sorted staticmethod 
str sum super tuple type vars zip 
Anzahl der Funktionen in Python: 75
'''
print('Anzahl der Funktionen in Python:', c)    # 75

'''
# 17 Funktionen am 21 & 22-02-2023
abs()
bin()
bool()
divmod()
hex()
input()
len()
list()
oct()
pow()
print()
range()
round()
str()
type()
'''