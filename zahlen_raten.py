import random

secret_number = random.randint(1, 100)

print("Random number generated! Good luck with your choice ;)")

chosen_number = input("guess my number: ")
print(f"you've chosen {chosen_number}!")


if int(chosen_number) > secret_number:
    print("you're thinking too big my friend!")
elif int(chosen_number) < secret_number:
    print("oh damn, that's lower than expected :(")
else:
    print("JAAAAAAAAAAAAAAAAAAACKPOT!!!!")

richtig = False

while not richtig:
    chosen_number = int(input("guess my number: "))
    if chosen_number < secret_number:
        print("think bigger!")
    elif chosen_number > secret_number:
        print("you're thinking too big my friend!")
    else:
        print("JAAAAAAAAAAAAAAAAAAACKPOT!!!!")
        richtig = True
# Hallo ich sehe dich
