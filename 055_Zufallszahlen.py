
# *** 055_Zufallszahlen ***

from random import randint
# randint(ANFANG, ENDE)
# ANFANG & ENDE sind inklusiv

wochentag = randint(1, 7)
print(wochentag)

if wochentag == 1:
    print('Montag')
elif wochentag == 2:
    print('Dienstag')
elif wochentag == 3:
    print('Mittwoch')
elif wochentag == 4:
    print('Donnerstag')
elif wochentag == 5:
    print('Freitag')
else:
    print('Endlich Wochenende')
