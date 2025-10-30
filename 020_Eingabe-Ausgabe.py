# *** input-Output - Eingabe-Ausgabe

print('Hello',  'Dracula')  # Hello Dracula

wort1 = 'Hello'
wort2 = 'I am Bond,'
wort3 = 'James Bond'
print(wort1, wort2, wort3)          # Hello I am Bond, James Bond

# standard separator (a single space) can be changed
print(1, 2, 3, sep='-')     # 1-2-3
print(6, 7, 8, sep='')      # 678


# the standard end is a return charachter (new line)
# one can change this to something else
print(1, end=' ')
print(2)            # 1 2
print(1, 2, end='\n')   # 1 2
print(3)                # 3 (on a new line)

# input()
# returns (accepts?) a string
name = input('Bitte den Namen eingeben!')
print('Hallo', name)
print(type(name))           # <class 'str'>

# to pause the execution...
# print() kann benuzt werden um Programmausführung zu pausieren
input()     # program stops and waits for Enter key
# gleich wie (aber freundlicher unten)...
input('Press Enter to continue...')     # program stops and waits for Enter key

# expand to show
anrede = input('Bitte die Anrede eingeben!')
vorname = input('Bitte den Vornamen eingeben!')
nachname = input('Bitte den Nachnamen eingeben!')
print('Hallo,', anrede, vorname, nachname)


