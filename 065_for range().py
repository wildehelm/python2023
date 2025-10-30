
# *** 065_for range() ***
# 2023-02-21
# for ist eine Schhleife zum Durchlaufen von Iterables/n

# for mit Liste
# heisst woanders (z.B. in PHP) 'for each loop'
tiere = ['Hund', 'Katze', 'Maus']
for tier in tiere:
    print(tier, end = ' ')  # Hund Katze Maus (inkl. letztes Leerzeichens vergl. 020_Eingabe_ausgabe)
print()
# OR...
for tier in tiere:
   print(tier)             # Hund Katze Maus, aber dann untereinander: vergl. 020_Eingabe_ausgabe
print()

# for mit String
for letter in 'abcdefghijklm':
    print(letter, end=' ')  # a b c d e f g h i j k l m
print()

# range()
# ANFANG ist inklusiv und ENDE ist exklusiv
# der ANFANG ist optional, und der Standard ist 0.
# das ENDE ist nicht optional
r = range(10)
print(type(r))      # <class 'range'>
print(r)            # range(0, 10)
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(-4, 4)))  # [-4, -3, -2, -1, 0, 1, 2, 3]
# Schrittweite
print(list(range(0, 10, 3)))  # [0, 3, 6, 9]
print(list(r))
# negative Schrittweite
print(list(range(20, 10, -3)))  # [20, 17, 14, 11]

# for mit range: count loop
for i in range(10):
    print('Hello', i+1, end=' ')  # Hello 1 Hello 2 Hello 3 Hello 4 Hello 5 Hello 6 Hello 7 Hello 8 Hello 9 Hello 10
    # print('Hello', i, end=' ') # Hello 0 Hello 1 Hello 2 Hello 3 Hello 4 Hello 5 Hello 6 Hello 7 Hello 8 Hello 9
    # print('Hello', end=' ')   # Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello
print()

# if the counter is not being used, Python coders often use _ as name
for _ in range(10):
    print('Hello', end=' ')   # Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello
print()

# using the i
for i in range(10):
    print(i, end=' ')   # 0 1 2 3 4 5 6 7 8 9
print()

# skip, user defined list
for i in range(0, 8, 2):
    print(i, end=' ')   # 0 2 4 6
print()

# example 4
for i in range(20, 9, -2):  # (20, 8, -2) would deliver the same result
    print(i, end=' ')   # 20 18 16 14 12 10
print()

# there might be a shuffle method to unsort lists, using random
# https://www.w3schools.com/python/ref_random_shuffle.asp