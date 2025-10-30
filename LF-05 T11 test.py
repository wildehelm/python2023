"""
#Aufgabe: Es gibt im Einzelhandel verschiedene Rabatte für den Preis je nach

#Umsatz (Einkaufsvolumen).
Es existiert folgende Staffelung der Rabatte:

#Umsatz < 100€      0%

#von 100 bis 250€   2%

#von 251 bis 500€   5%

#von 501 bis 1000€  10%

#ab 1001€           12%


#ACHTUNG: % Zeichen in Python heißt Modulo, nicht %!
"""

# EINGABE
x=""
i=0

while i<10:
    try:
        x=float(input("Geben Sie den Betrag (€,cc Umsatz) ein: "))
        break
    except:
        x="error"
        print("Etwas stimmt nicht ganz. Bitte versuchen Sie es noch mal(",i+1,")")
    
# VERARBEITUNG
if x < 100:
    Rabatt=int(0)
elif x < 251:
    Rabatt=int(2)
elif x < 501:
    Rabatt=int(5)
elif x < 1001:
    Rabatt=int(10)
else:
    Rabatt=int(12)
    
PreisNachRabatt = x - (x*Rabatt/100)     # PreisNachRabatt = float(x - (x*Rabatt/100))

# AUSGABE
if Rabatt > 0:
    print("Für Ihren Einkauf in Volumen von str.format{x:.2f}, € bekommen Sie Rabatt in Höhe von", Rabatt, "% und Sie zahlen nur noch", PreisNachRabatt, "€.")
else:
     print("Für Ihren Einkauf in Volumen von" , x,
      "€ bekommen Sie leider keinen Rabatt.")
