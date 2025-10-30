# *** arithmatic operators ***

print(7 + 3)        # 10
print(10 - 3)       # 7
print(9 * 3)        # 27
# division always returns a float (unlike Java)
print(9 / 3)        # 3.0

# Integer-Division - floor division - the english term is more accurate: //
# these are first divided, then rounded
print(9 // 3)       # 3
print(11 // 3)      # 3 (decimals are discarded)
# but, when one of the operands is a float, the result is a float, too... potentially leading to calculation errors
print(11 // 3.0)    # 3.0
print(11.0 // 3)    # 3.0

# mod - Modulo - die Restwertdivision: %
print(10 % 3)       # 1
print(11 % 4)       # 3
print(7 % 7)        # 0
# if the first number is smaller as the second...
print(4 % 7)        # 4
# gerade / ungerade Zahlen finden
print(17 % 2)       # either 1 or 0. If 1, the tested number is uneven, if 0, the number is even
print(17 % 0)       # ZeroDivisionError: integ€er modulo by zero

# potenzoperator: **
print(2 ** 3)       # 8
print(2 ** 8)       # 256
print(2 ** 10)      # 1024
print(2 ** 16)      # 65536
print(2 ** 24)      # 16_777_216 (Number of colours computers can display)
print(2 ** 32)      # 4.2-4.3 Milliarden (number of possible IPv4 addresses) - compare max size of integer in Java


