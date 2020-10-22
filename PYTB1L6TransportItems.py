#PYTB1L6TransportItems

import os
import time

#List of Lists
factory = ["product"]
distribution = []
shop = []

#Product transport

run = True
while run == True:
    os.system("cls")
    print("Factory:", factory)
    print("distribution", distribution)
    print("Shop", shop)
    time.sleep(2)

    distribution.extend(factory)
    factory.remove("product")
    os.system("cls")
    print("Factory:", factory)
    print("distribution", distribution)
    print("Shop", shop)
    time.sleep(2)

    shop.extend(distribution)
    distribution.remove("product")
    os.system("cls")
    print("Factory:", factory)
    print("distribution", distribution)
    print("Shop", shop)
    time.sleep(2)

    antwoord = input("Nog een keer [J/N]")
    if antwoord.lower() == "j":
        factory.append("product")
        shop.clear()
        run = True
        os.system("cls")
    else:
        run = False
    
