# *** 090_Zahlensysteme ***
# 2023-02-22

# binary - binär (b | B)
# Mögliche Ziffern: 0, 1
print('binary - binär (b | B)')
print(0b10)     # 2
print(0b10001)     # 17
print(bin(17))     # 0b10001
print(type(bin(17)))    # <class 'str'>
print(type(0b10001))    # <class 'int'>
print()

# hexadecimal - Hexadezimal (x | X)
# Mögliche Ziffern: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
print('hexadecimal - Hexadezimal (x | X)')
print(0x1)     # 1
print(0x10)     # 16
print(0x1d)     # 29 = 1*16 + d(13)*1
print(0x2f)     # 47 = 2*16 + f(15)*1
print('Weiter geht\'s für Thomas')
print(0x100)    # 256 = 1*(16 * 16) = 1 * 256       # just like print(0x10 * 0x10)
print(0x3a7)    # 936 = 3*256 + a(10)*16 + 7*1
print(hex(16))  # 0x10
print()

# octal - Octal (o | O)
print('octal - Octal (o | O)')
print(0o10)     # 8
print(0o33)     # 27 3*8 + 3*1
print(oct(27))  # 0o33
print()

'''
123 Dezimal:        1*10^2 + 2*10^1 + 3*10^0
123 Hexadezimal: 1*16^2 + 2*16^1 + 3*16^0
101 Binär:              1*2^2 +  0*2^1 +  1*2^0
'''
