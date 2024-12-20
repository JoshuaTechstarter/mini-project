# Aufgabe 1: Primzahlenfinder (aufgabe1_primzahlen.py)
# Schreibt ein Programm, das überprüft, ob eine eingegebene Zahl eine Primzahl ist. Eine
# Primzahl ist nur durch 1 und sich selbst teilbar.


def is_prime(number):
    if number == 0:
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


i = int(input("number ? "))
print(is_prime(i))
