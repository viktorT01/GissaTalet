import random

tal = random.randint(1,10)

gissning = input("Gissa ett tal mellan 1 och 10: ")
gissning = int(gissning)

if gissning == tal:
    print("Rätt!")
else:
    print("Tyvärr, det var", tal)