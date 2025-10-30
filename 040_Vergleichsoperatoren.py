
# *** 040_Vergleichsoperatoren ***
# auch relationale Operatoren genannt
# evaluieren zu einem Boolean

# >, <, >=, <=, !=
print(7 == 8)       # False
print(7 != 8)       # True

# verkettete Vergleiche
print(1 < 4 < 7)    # True
print(11 > 4 < 7)    # True

# mehrere Werte gleichzeitig vergleichen
a, b, c, = 1, 2, 3
print((a, b, c) == (1, 2, 3))   # True
print((a, b, c) == (1, 4, 3))   # False

# Stringvergleiche (der ASCII-Wert ist entscheidend)
print('a' < 'b')                # True
print('c' < 'b')                # False
print('A' < 'b')                # True
print('Z' < 'a')                # True
print('Hello' > 'Hallo')        # True
# Wenn das erste Zeichen gleich ist, wird das zweite verglichen usw.

