user_input = input(print("\nGib einen Satz ein und ich zähle die Wörter"))

print(f"Dein Satz ist: \n {user_input}")

ergebnis = user_input.count(" ") + 1

print("\nDie Anzahl der Wörter beträgt : \n" + str(ergebnis))
