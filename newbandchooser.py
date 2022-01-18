import random 
with open('bands.txt') as b:
    bands = [line.rstrip() for line in b]
print(bands[random.randint(0, len(bands)-1)])