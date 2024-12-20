# Aufgabe 5: Bestimmen, ob eine eingegebene Zahl gerade oder ungerade ist.

print ("Prüfung, ob eine Zahl gerade oder ungerade ist")
print ("")
zahl=input("Welche Zahl soll überprüft werden? ")
x=float(zahl)

if x % 2 == 0:
    print ("Deine Zahl ist gerade")
elif x % 2 == 1:
    print ("Deine Zahl ist ungerade")    
else:
    print("Das war Quatsch!")
