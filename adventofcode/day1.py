import math
f = open('C:\\Users\\bobei\\small-python-projects\\adventofcode\\input.txt')
lines = (f.readlines())
total = 0
part1 = 0
def fuelcalc(mass):
    return int(mass)//3-2

for i in lines:
    req = fuelcalc(i)
    part1 += req
print(part1)

# def part1():
#     for i in lines




#     fuel = fuelcalc(mass)
#     total += fuel


#     while fuel > 0:

#         fuel = fuelcalc(fuel)
#          total += fuel
for i in lines:
    

    fuel = fuelcalc(i)
    while fuel > 0:
        total += fuel
        fuel = fuelcalc(fuel)
f.close()
print(total)

# def iterative_fuel_calc(mass: int) -> int:
#     total = 0
#     requirement = fuelcalc(mass)
#     while requirement > 0:
#         total += requirement
#         requirement = fuel_requirement(requirement)
#     return total