import random

tal = random.randint(1,10)

for i in range(3):
    gissning = input(f"Försök {i+1}, gissa talet: ")
    gissning = int(gissning)
    if gissning == tal:
        print("Rätt gissat!")
        break
    else:
        print("Fel gissat.")