"""
#Aufgabe
Erstelle ein Python-Programm zur Berechnung des Bedarfs an Wandfarbe
„Alpina Weiß“ für einen rechteckigen Raum (BxLxH in m).
Der Benutzer soll die Maße des Raums in Metern mit einer Kommastelle
eingeben. Eine 10 l „Alpina weiß“-Eimer kostet (Stand 2020) 29,19 €
inkl. MwSt. und wird pro Anstrich 160ml/m² verbraucht. Als Vereinfachung
werden Fenster und Türen des Raums vernachlässigt bzw. dient die
überschüssige Farbe als Reserve für Nachbesserungen.

Wie viele Eimer-Farbe muss der Anwender kaufen und wie viel kostet es?
"""

# a = Breite in cm
# b = Länge in cm
# c = Höhe in cm
# d = ml pro m² deckungskraft


import math

a=float(input("Bitte die Breite des Raumes in m eingeben. Benutzen Sie bei Bedarf eine Kommastelle: "))
b=float(input("Bitte die Länge(Zahl) des Raumes in cm eingeben. Benutzen Sie bei Bedarf eine Kommastelle: "));
c=float(input("Bitte die Höhe(Zahl) des Raumes in cm eingeben. Benutzen Sie bei Bedarf eine Kommastelle: "))
d=float(input("Bitte auf dem Behälter ablesen und Deckungsbereich (ml pro m²)(Zahl) eingeben: "))   
v=float(input("Wieviel Liter in einem Behälter? (z.B. 10): "))

# verarbeitung
A=2*(a*c)+2*(b*c)   # zu farbende Oberfläche
B=(1000*v)          # soviel ml in einem Behälter
C=B/d               # Anstrichfläche aus einem Behälter
D=A/C               # so viel Behälter brauchst du, aber bitte nach oben runden
P=math.ceil(D)*29.19

# ausgabe
print('Die Oberfläche die zu farben sind, sind', round(A,2), 'm²')
print('Mit einem Behälter wie diese können Sie einmal', round(C,2), 'm²', 'abdecken.')
print('Sie brauchen deswegen', math.ceil(D), 'Behälter. Die Farbe kostet insgesamt', P)

