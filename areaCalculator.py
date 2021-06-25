class RegShape:
    def __init__(self, length, num_sides):
        self.length = length
        self.sides = num_sides

    def perimeter(self):
        print(f'The perimeter is {self.length * self.sides} units')


class IrregShape:
    def __init__(self, length):
        self.length = length

    def perimeter2(self):
        perimeter = 0

        for i in self.length:
            perimeter +=i
        print(f'the perimeter is {perimeter} units')


shape = int(input('type 1 if your shape is regular (all sides the same size) and 2 if it is not'))

if shape == 1:
    length = int(input("Enter the length of the shape"))
    sides = int(input('Enter the amount of sides'))

    s = RegShape(length, sides)
    s.perimeter()
else:
    sides = int(input('enter the amount of sides the shape has'))
    lengths = []
    for i in range(sides):
        l = int(input('Enter length'))
        lengths.append(l)
    s = IrregShape(lengths)
    s.perimeter2()






