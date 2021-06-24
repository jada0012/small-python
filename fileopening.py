num =[i for i in range(1,100)]

with open('numlist.txt', "w") as n:
    for i in num:
        n.write(str(i))
        n.write("\n")

with open('numlist.txt', 'r') as n:
    numlst = [line.rstrip() for line in n]

for i in numlst:
    print(i)