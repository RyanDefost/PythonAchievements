#Zoeken naar Waldo

import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)


stoelnummer = -1
for x in range(len(people)):
    if people[x] == "Waldo":
        stoelnummer = x

print(people)
print("waldo zit in stoel Nr." + str(stoelnummer))

