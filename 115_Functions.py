# *** 115_Functions.py ***
# 2023-02-23

# procedural programming - prozeduraler Programmierung
# ist eine Funktion ohen Rückgabewert

# Schlüsselwort zum Erzeugen einer Funktion: def
# Vorteile:
# * können mehrfach ausgeführt werden (ohne es mehrmals zu typen)
# * Funktionen haben einen eigenen Gültigkeitsbereich (variablen können lokal definiert werden)

# Funktionsbezeichner
print('Funktionsbezeichner')
# Imperativ (Handlungsaufforderung), der die Funktionalität bescheriebt
# Nomen, das den Rückgabewert beschreibt

# Funktionsdefinition
print('Funktionsdefinition...')


def meine_zweite_funktion():
    print('Hallo, ich bin deine Funktion.')
    print('Was kann ich für dich tun? ')

# Funktionsaufruf
print('Funktionsaufruf...')
meine_zweite_funktion()

# Parameter und Argumente
# Parameter sthen in der F-definition
# ist wie eine Variable, die nur in der Funktion gültig ist


def greet(para):
    print('Hello', para)

print('Parameter und Argumente...')

greet('Peter')      # Hello Peter
greet('Paul')       # Hello Paul
greet('Mary')       # Hello Mary
greet('')           # Hello
# greet()             # TypeError: greet() missing 1 required positional argument: 'para'
print()

# return
# zum Zurückgeben von Werten aus Funktionen
print('function with return...')


def addiere1(x, y):
    ergebnis = x + y
    return ergebnis

print(addiere1(3, 4))    # 7
zahl = addiere1(23, 42)
zahl += 3
print(zahl)             # 68

# standard parameters
# allen Parametern, die keinen Standardwert haben, muss ein Argument übergeben werden
# die Parameter mit den Standardwerten müssen am Ende stehen
print('default/standard parameters...')


def addiere2(x, y=1):
    return x + y

print(addiere2(7))          # 8
print(addiere2(14, 28))     # 42

# Exkurs
# sehe .py vom Dozenten
