with  open("C:\\Users\\bobei\\python\\small-python-projects\\aoc2020\\input1.txt") as file:
    lines = [line.rstrip() for line in file]

for i in range(199):
    lookup = 2020- int(lines[i])
    if str(lookup) in lines:
        index = lines.index(str(lookup))
        
        prf = int(lines[index]) * int(lines[i])
        print(prf)
        break

for i in range(199):
    l2 = 2020-int(lines[i])
    for num1 in lines:
        for num2 in lines:
            if int(num1) + int(num2) ==l2:
                end = int(num1) * int(num2) * int(lines[i])
                print(end)
                break





    

# steps
# find the lookup
#