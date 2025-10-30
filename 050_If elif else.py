
# *** 050_If elif else ***

x = 7
print('if ohne else...')
if x == 7:
    print('Ja, x ist gleich 7')

# else
print('if mit else...')
if x == 8:
    print('Ja, x ist gleich 8')
else:
    print('Nein, x ist nicht gleich 7')

# elif
print('if mit elif und else...')
x = 9
if x == 8:
    print('Ja, x ist gleich 8')
elif x == 9:
    print('Ja, x ist gleich 9')
else:
    print('Nein, x ist nicht gleich 8 oder 9')
    x = 9
    print('Jetzt ist x aber gleich 9!')

