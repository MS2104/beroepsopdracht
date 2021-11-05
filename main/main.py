import time
from typing import Text

def intro():
    print("Text based application eindopdracht door Milad SD1D")
    print('''
    Je begint in Syrië. 
    Het is een vredige dag, en zit in de klas. Terwijl de leraar uitleg aan het geven is hoor je explosies, 
    de grond tilt en de ramen gaan kapot. Glasscherven vliegen door de kamer en je hoort gegil overal om je heen,
    Je gaat op de grond liggen samen met je klasgenoten.
    ''')

    print("Je ouders hebben er genoeg van en besluiten om te vluchten en jij gaat met ze mee.")

def firstchoice():
    stuff = ["knuffel", "kleren", "speelgoed"]
    carrying = 0
    inventory = []
    print("Het is tijd om in te pakken.")
    print(stuff)
    packstuff = input('''Wat neem je me? Kies 2 items.
    > ''')
    
    while carrying <= 2:
        if packstuff == 'knuffel':
            if carrying == 2:
                print("Je tas zit al vol!")
                break
            elif carrying <= 2:
                print('Je neemt ', packstuff, ' met je mee.')
                break
        elif packstuff == 'kleren':
            if carrying == 2:
                print("Je tas zit al vol!")
                break
            elif carrying <= 2:
                print('Je neemt ', packstuff, ' met je mee.')
                break
        elif packstuff == 'speelgoed':
            if carrying == 2:
                print("Je tas zit al vol!")
                break
            elif carrying <= 2:
                print('Je neemt ', packstuff, ' met je mee.')
                break

# APPLICATION LOOP STARTS HERE!

running = True
while running:
    intro()
    firstchoice()

    while True:
        print("Wil je het opnieuw doen?")
        tryagain = input("J/N? > ")
        if tryagain == 'J' or 'j':
            break
        elif tryagain == 'N' or 'n':
            print("Bedankt voor het spelen!")
            time.sleep(3)
            running == False