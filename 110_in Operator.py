# *** 110_in Operator ***
# wilhelm
# 2023-02-23

# tests if a value appears in a sequence
# Tested, ob eine Wert in einer Sequenz vorkommt.
# ist eine der Vergleichsoperatoren und evaluiert zu einem Boolean.
# Eher selten in anderen Programmiersprachen, gibt es aber in SQL

list = [1, 4, 7, 9]
print(4 in list)    # True
print(6 in list)    # False

x = 7
if x in list:
    print('Treffer!')   # Treffer!

#  example 2 -
#  häufig ein guter Ersatz für "or":
print('test if x in y')
zahl = 11
print(zahl == 7 or zahl == 11 or zahl == 19)    # True
print(zahl in [7, 11, 19])                      # True, but better
print(zahl in [7, 19])                          # True, and can be extended easier than adding or ... or ...
print()


# not in
print('not in and not ( in )')
liste = [1, 4, 7, 9]
print(3 not in list)
print(not (3 in list))
print()

# in operator and strings
print('in operator and strings')
print('e' in 'Hello')       # True
print('a' in 'Hallo')       # True
print('a' not in 'Hello')   # True
print('Hell' in 'Hello')    # True
print()
