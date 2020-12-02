from turtle import *
slength = 1000

# def square(sidelength=slength):
#     for i in range(4):
#         forward(sidelength)
#         right(90)
# num= 5
# for i in range(60):
#     square(num)
#     right(5)
#     num+=10
def star(sidelength=100): 
    for i in range(5):
        left(-144)
        forward(sidelength)
        
num = 25
speed(10)     
for i in range(45):
    star(num)
    right(8)
    num +=5
