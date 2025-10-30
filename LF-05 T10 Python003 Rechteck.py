#eingabe
#Berechnung der Fläche und Umfang eines Rechtecks
# a = Breite in cm
# b = Höhe in cm
a=float(input("Bitte die Breite (Zahl) des Rechtecks in cm eingeben: "))
b=float(input("Bitte die Höhe(Zahl) des Rechtecks in cm eingeben: "))

# verarbeitung
A=a*b
U=2*a+2*b       # or: = 2*(a+b)

# ausgabe
# python adds space character before output when you use the a, b, c syntax!
print("Die Fläche des Rechtecks beträgt ", A, "cm²." )
# python adds space character before output/ between elements, regardless of how many YOU add!
print("Der Umfang des Rechtecks beträgt", U, "cm." )         
# it is important to add empty space when you use the a + b + c syntax!
print("Der Umfang des Rechtecks beträgt "+str(U)+" cm." )

