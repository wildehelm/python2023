# *** 080_continue and break ***
# 2023-02-22

# break
# beendet sofort die (jetzige) Schleife
from random import randint
for i in range(1, 10_000):
    if randint(1, 6) == 6:
        print(i)
        break

# endless loop with pass - per WHILE
i = 0
while True:
    # pass
    x = randint(1, 6)
    print(x)
    i += 1
    if x == 6:
        print('Versuchnr.', i)
        break

# continue
for i in range(70, 80):
    if i == 74:
        continue    # go back to where loop started and continue from there
    print(i, end=' ')   # 70 71 72 73 75 76 77 78 79
print()

# ende