"""Programm zur Berechnung einer Binärzahl
mit der Divisions-Methode inkl. Rest"""

#EINGABE
gZahl=int(input("Bitte eine ganz Zahl eingeben: "))

#VERARBEITUNG
Quotient=gZahl
while Quotient>0:
    Rest=Quotient%2
    Quotient=int(Quotient/2)             #Quotient muss ganze Zahl sein
    print(Quotient," R ", Rest)

#AUSGABE
print("Die Binärzahl von",gZahl," ist",bin(gZahl))
