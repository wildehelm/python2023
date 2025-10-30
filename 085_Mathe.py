
# *** 085_Mathematik ***
# 2023-02-22

# pow()
# power - Hochrechnung
print(pow(2, 8))    # 256
print(2 ** 8)       # 256

# abs()
# absolute number - Betrag
print((abs(-10)))   # 10

# divmod()
# division and modulo in one
print(divmod(13, 5))    # (2, 3)

# round(zahl [, Stellen])
# Das in den eckigen Klammer ist optional (In der BNF Backus-Naur-Form festgelegt)
# https://de.wikipedia.org/wiki/Backus-Naur-Form
print('Einleitung zu Runden')
print(round(4.497))      # 4
print(round(4.497, 0))      # 4.0
print(round(4.497, 1))      # 4.5
print(round(4.447, 2))      # 4.45
print('das war die Einleitung')

# .5 wird mathematisch gerundet (nicht kaufmännisch)
# .5 rundet zur GERADEN GANZEN Zahl
print('.5 rundet zur GERADEN GANZEN Zahl')
print(round(0.5))   # 0
print(round(1.5))   # 2
print(round(2.5))   # 2
print(round(3.5))   # 4
print(round(4.5))   # 4
print('das war .5 rundet zur GERADEN GANZEN Zahl')
# aber...
print('aber...')
print(round(0.51))   # 1
print(round(1.51))   # 2
print(round(2.51))   # 3
print(round(3.51))   # 4
print(round(4.51))   # 5
print('das war aber...')

# kaufmännisches Runden
print('kaufmännisches Runden...')
print(int(0.5 + 0.5))   # 1
print(int(1.5 + 0.5))   # 2
print(int(2.5 + 0.5))   # 3
print(int(3.5 + 0.5))   # 4
print(int(4.5 + 0.5))   # 5
print('Das war # kaufmännisches Runden')

import math     # the import should be in the beginning. the IDE reminds us
print('rounding with ceil() after importing math')
print(math.ceil(9.1))   # 10
print(math.ceil(-9.1))   # -9

# abrunden mit floor() Richtung Minus-Unendlich
print(math.floor(9.8))   # 9
print(math.floor(-9.8))   # -10

# sqrt - Quadratwurzel
print(math.sqrt(64))    # 8.0

# Pi - 22/7
print(math.pi)          # 3.141592653589793