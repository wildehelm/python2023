"""
#Aufgabe: Es gibt im Einzelhandel verschiedene Rabatte für den Preis je nach

#Umsatz (Einkaufsvolumen).
Es existiert folgende Staffelung der Rabatte:
Umsatz < 100€      0%
von 100 bis 250€   2%
von 251 bis 500€   5%
von 501 bis 1000€  10%
ab 1001€           12%
#ACHTUNG: % Zeichen in Python heißt Modulo, nicht %!
"""

#Antwort=0
Aufforderung="Geben Sie den Betrag (€ Umsatz) ein: Benutzen Sie dabei einen '.' (Punkt) für die Kommastelle: "


# EINGABE
while True:
    try:
        Antwort=input(Aufforderung)
        x=float(Antwort)
        break
    except:
        print("Sie haben '"+ Antwort +"' eingegeben.")
        print("Etwas stimmt nicht ganz. Bitte versuchen Sie es noch mal.")
        #print(Aufforderung)
    
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
    print("Für Ihren Einkauf in Volumen von" , x,
      "€ bekommen Sie Rabatt in Höhe von", Rabatt, "%", "(" +str(x*Rabatt/100) +" €)")
    print("Sie müssen nur noch", PreisNachRabatt, "€ zahlen.")
else:
     print("Für Ihren Einkauf in Volumen von" , x,
      "€ bekommen Sie leider keinen Rabatt.")

print("Programmende")
