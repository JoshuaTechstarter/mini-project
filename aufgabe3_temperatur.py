
user_input = float(input('Gib bitte die Temperatur die in Fahrenheit umgerechnet werden: '))

def celsius_to_fahrenheit():
    fahrenheit = (user_input * 9/5) + 32
    print(f'{user_input} Grad Celsius sind {fahrenheit} Grad Fahrenheit.')

celsius_to_fahrenheit()

                