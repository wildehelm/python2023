
# *** 060_Listen - Lists and arrays ***
# in anderen Sprachen meist das (nummerische) Array (PHP, Java)
# 2023-02-21

x = [1, 7, 9, 12]
print(type(x))      # <class 'list'>
print(x)            # [1, 7, 9, 12]

# Indexing
print(x[2])         # 9
print(x[0])         # 1
# print(x[9])         # IndexError: list index out of range

# Negative Indexe
print(x[-1])        # 12

# Slicing
# ANFANG ist inklusif und ENDE exklusiv
print(x[1:3])       # [7, 9]
# without defining the last index
print(x[1:])        # [7, 9, 12]
# when using an index greater than the last (no error)
print(x[1:10])      # [7, 9, 12]

# list() function
list2 = list('Hello')
print(list2)        # ['H', 'e', 'l', 'l', 'o']

# Empty lists - Leere Listen
list3 = []
list4 = list()
print(list3, list4)  # [] []

# Listen können alle Datentype, auch gemischt, beinhalten
list5 = [True, 23, 7.7, 'Hello', [7, 11]]
print(list5)        # [True, 23, 7.7, 'Hello', [7, 11]]

# Mehrdimensionale Listen
list6 = [1, 2, 3, [4, 5]]
print(list6)        # [1, 2, 3, [4, 5]]
print(list6[3][0])  # we wanted 4
print([4, 5][0])    # 4 (but would not be hard coded this way)

list7 = [1, 2, [3, 4, 5, [7, 8, 9]]]
print(list7[2][3][1])   # we were looking for the 8
list7 = [
    1,
    2,
    [
        3,
        4,
        5,
        [
            7,
            8,
            9
        ]
    ]
]

# len function
# returns the length of a container
list8 = [1, 4, 6, 14]
print(len(list8))   # 4

# Listen-Methoden - list methods
# append(): adds a new element to the end
list8 = [1, 2, 3, 4]
print(list8)
list8.append(5)     # add a 5 to the end
print(list8)
# eine Liste ist ein Element, wie jedes andere auch
# und dadurch entsteht eine zwei-dimensionale Liste:
list8.append([6, 7, 8])
print(list8)        # [9, 1, 2, 3, 4, 5, [6, 7, 8]]

# insert(n, x)
# insert to add element x to the list at position n
list8.insert(0, 9)
print(list8)        # [9, 1, 2, 3, 4, 5]


# count(e)
# how many times does an element occur?
print([1, 2, 3, 1, 2, 1, 3, 1].count(1))    # 4

# index(e)
# ermittellt die erste Position vom Element:
print([1, 2, 3, 1, 2, 1, 3, 1].index(3))    # 2
print(type([1, 2, 3, 1, 2, 1, 3, 1].index(3)))  # <class 'int'>
# when the given value is not in the list...error expected:
# print([1, 2, 3, 1, 2, 1, 3, 1].index(9))    # ValueError: 9 is not in list

# pop([n])
# Gib das Element an der Position n zurück
# UND entfernt es aus der Liste (destructive)
# der Standard ist das letzte Element
list8 = [1, 2, 3, 4]
print(list8.pop())      # 4
print(list8)            # [1, 2, 3] (4 is gone)
list8.pop()
print(list8)            # [1, 2] (3 is also gone)
# storing the removed value in a variable when removing
wert = list8.pop()
print(wert)             # 2
print(list8)            # [1]

# remove(e)
# only the first instance is removed
list9 = [1, 2, 3, 4, 5, 4, 7]
list9.remove(4)
print(list9)        # [1, 2, 3, 5, 4, 7]

# reverse()
list9.reverse()
print(list9)        # [7, 4, 5, 3, 2, 1]
listABC = ['Aa', 'Bb', 'Cc']
listABC.reverse()
print(listABC)          # ['Cc', 'Bb', 'Aa']

# sort()
print(list9)        # [7, 4, 5, 3, 2, 1]
list9.sort()
print(list9)        # [1, 2, 3, 4, 5, 7]

# extends(e)
# adds the content to a list, but not as a sub list like in append
list10 = [1, 2]
list10.extend([3, 4, 5])
print(list10)   # [1, 2, 3, 4, 5] instead of [1, 2, [3, 4, 5]]
list10.extend('Hallo')
print(list10)   # [1, 2, 3, 4, 5, 'H', 'a', 'l', 'l', 'o']
# play with sort
# list10.sort() # Note: You cannot sort a list that contains BOTH string values AND numeric values.

# clear()
# empties the list
list10.clear()
print('List:', list10)   # []
print(len(list10))       # 0

# open 025_String of lecturer and see an example pertaining the len function, which he's adding now