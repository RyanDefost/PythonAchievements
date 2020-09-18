# hoger lager spelletje maken
# Nieuw stof gebruiken (If ,elif en else + en of)

# Doel:
# Speler krijgt een getal van 1 tot 10
# Speler moet aangeven of het hoger of lager is
# Je wint of verliest (of gelijkspel)

import random

willekeur = random.randrange(1, 11)
print("je getal is", willekeur)
print ("Wordt het volgende getal hoger of lager?")

nieuwWillekeur = random.randrange(1, 11)

antwoord = input(": ")
if antwoord == "hoger" and (nieuwWillekeur > willekeur):
    print("inderdaad!")
elif antwoord == "lager" and (nieuwWillekeur < willekeur):
    print("inderdaad")
else:
    print("helaas niet")
