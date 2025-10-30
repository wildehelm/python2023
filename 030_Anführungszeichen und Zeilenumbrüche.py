
# *** 030_Anführungszeichen und Zeilenumbrüche ***

# einfache und duppelte AFZ sind glecihwertig
print("Hello World1")       # Hello World1
print('Hello World2')       # Hello World2

# Zeilenumbrüche in der Ausgabe
print('So funktioniert ein\nZeinenumbruch.')       #

print('''Dies beinhaltet auch
einen Zeilenunbruch.''')

# if you want to add comments in a situation like this
s = 'Dieser Satz'       # jetzt kann in jeder Zeile ein Kommentar stehen
s += ' soll in einer Zeile'
s += ' ausgegeben werden.'
print(s)            # Dieser Satz soll in einer Zeile ausgegeben werden.

print('\\')         # \ (the first masks the second one)
# print('\\\')        # SyntaxError: unterminated string literal (detected at line 21)
print('\\\\')       # \\

# masking (Maskieren) or escaping apostrohes
print("Let's go")   # Let's go
print('Er sagte: "Hallo"')          # Er sagte: "Hallo"
print("Er sagte: \"Hallo\"")        # Er sagte: "Hallo"
print('He said: "Let\'s go"')       # He said: "Let's go"

