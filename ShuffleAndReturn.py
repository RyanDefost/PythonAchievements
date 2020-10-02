import random
import os

def shuffle(original):
    return(''.join(random.sample(original, len(original))))

os.system("cls")
print("---------------------------------------------------")
WOORD = input("welk woor wil je shuffle?: ")

antwoord = shuffle(WOORD)
os.system("cls")
print(antwoord)


print("---------------------------------------------------")
WOORD2 = input("Nog een!: ")

antwoord2 = shuffle(WOORD2)
os.system("cls")
print(antwoord2)


print("---------------------------------------------------")
WOORD3 = input("Nog één laatste keer!: ")

antwoord3 = shuffle(WOORD3)
os.system("cls")
print(antwoord3)
