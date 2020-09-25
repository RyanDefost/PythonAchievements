#Opdracht: 5 keuzes maken met meerdere antwoorden
#Hoeft geen invloed te hebben op volgende vraag

import os


print("Ik heb een aantal vragen voor je heb je zin om ze te beantwoorden?")

antwoord1 = input("ja of nee?: ")
if antwoord1.lower() == "ja":
    print("Oke tijd om te beginnen!")
elif antwoord1.lower() == "nee":
    print("ooh... WE BEGINNEN ALSNOG!")
else:
    print(antwoord1, "is geen geldig antwoord!")

os.system("cls")
print("\n-------------------------------------------------------")
print("Tijd voor de eerste vraag")
print("Welk cijfer kies je?\n:A\n:B\n:C")
antwoord2 =input("\nAntwoord: ")

if antwoord2.lower() == "a":
    print("Mooi getal")
elif antwoord2.lower() == "b":
    print("Mooi getal")
elif antwoord2.lower() == "c":
    print("Nee, fout!")
else:
    print(antwoord2, "is geen geldig antwoord!")
input("\n--NEXT--")

os.system("cls")
print("\n-------------------------------------------------------")
print("Tijd voor de tweede vraag")
print("Wat is 2+2*5?\n:20\n:12\n:9")
antwoord3 =input("\nAntwoord: ")

if antwoord3.lower() == "20":
    print("Nee je moet eerst keer doen")
elif antwoord3.lower() == "12":
    print("Ja inderdaad")
elif antwoord3.lower() == "9":
    print("Er staat een * niet +.")
else:
    print(antwoord3, "is geen geldig antwoord!")
input("\n--NEXT--")

os.system("cls")
print("\n-------------------------------------------------------")
print("Tijd voor de Laatste vraag")
print("Wat vond je van de vragen?\nGEWELDIG: A\nSaai en onorigineel: B\nantwoord C: C")
antwoord3 =input("\nAntwoord: ")

if antwoord3.lower() == "a":
    print("Correct!")
elif antwoord3.lower() == "b":
    print("jij bent onorigineel")
elif antwoord3.lower() == "c":
    print("Wat?")
else:
    print(antwoord3, "is geen geldig antwoord!")
