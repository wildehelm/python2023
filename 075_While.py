
# *** 075_While ***
# 2023-02-22
# solange

# While is especially useful if you don't know the number
# Mache etwas so lange es Donnerstag ist, ODER
# Versuche mich zu verbinden so lange ich nicht verbunden bin

# while as counted loops
i = 1
while i < 6:
    print(i, end=' ')   # 1 2 3 4 5
    i += 1
print()

for i in range(1, 6):
    print(i, end=' ')   # 1 2 3 4 5
print()

# dies geht nur mit while:
i = 1
while i < 100_000:
    print(i, end=' ')   # 1 2 6 42 1806
    i = i + i * i
print()

# continue & break... follows 080
