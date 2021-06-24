import random

with open('C:\\Users\\bobei\\python\\small-python-projects\\spanish\\noun.txt') as n:
    nouns = [line.rstrip() for line in n]
with open('C:\\Users\\bobei\\python\\small-python-projects\\spanish\\pronoun.txt') as n:
    pronouns = [line.rstrip() for line in n]
with open('C:\\Users\\bobei\\python\\small-python-projects\\spanish\\verb.txt') as n:
    verbs = [line.rstrip() for line in n]
with open('C:\\Users\\bobei\\python\\small-python-projects\\spanish\\object.txt') as n:
    objects = [line.rstrip() for line in n]
s = ['s', '']
neg = ['did not', '']
no = ['no', '']

for i in range(25):
    print('%s%s  %s %s the %s%s  ' %(random.choice(nouns), random.choice(s),random.choice(neg),random.choice(verbs), random.choice(objects), random.choice(s)))
    input()

for i in range(25):
    print(' %s%s %s %sed the %s%s' %(random.choice(nouns), random.choice(s), random.choice(neg), random.choice(verbs), random.choice(objects), random.choice(s)))
    input()


for i in range(25):
    print('%s%s has %s %sed the %s%s' %(random.choice(nouns), random.choice(s), random.choice(no), random.choice(verbs), random.choice(objects), random.choice(s)))
    input()


for i in range(25):
    print('%s%s will %s %s the %s%s' %(random.choice(nouns), random.choice(s), random.choice(no), random.choice(verbs), random.choice(objects), random.choice(s)))
    input()




