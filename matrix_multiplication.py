import numpy as np
import pyinputplus as pyin
print("multiplying matrices is hard, but this will do it for you guaranteed. \nRules: \n1. Matrices are written in the format rows by columns, eg a 2x4 matrix has two rows and four columns \n2. for two matrices to be successfully multiplied, the columns in the first must be equal to the number of rows in the second. \n3. When entering your matrices enter them left to right, top to bottom as you read them.")

def get_input():
    x1=pyin.inputInt("enter the number of rows in the first matrix: ", min=1)
    y1=pyin.inputInt("enter the number of columns in the first matrix: ", min=1)

    x2=pyin.inputInt("enter the number of rows in the second matrix: ", min=1)
    y2=pyin.inputInt("enter the number of columns in the second matrix: ", min=1)
    return x1, y1, x2, y2

def generate_matrices(x, y):
    matrix=np.zeros(x*y).reshape(x,y)
    print("matrix:")
    for i in matrix:
        print(i)


def get_matrix_values(x,y):
    vals = []
    for i in range(x*y):
        num = pyin.inputNum("enter a number")
        vals.append(num)
    val_arr = np.array(vals).reshape(x,y)
    for i in val_arr:
        print(i)
    return val_arr

x1, y1, x2, y2 = get_input()
while y1 != x2:
    print("your values are wrong, remember rule 2 (num cols m1 == num rows m2) ")
    x1, y1, x2, y2 = get_input()   

generate_matrices(x1, y1)
generate_matrices(x2, y2)

m1 = get_matrix_values(x1,y1)
m2 = get_matrix_values(y2,x2)

#i'm gonna have to use a for loop somehow
output = []
for i in range(x1*y2):
    v = m1[0] * m2[0]
    print(f'{m1[0]=},{m2[0]=}, {v=}')
    output.append(sum(v))
    print(f'{output=}')
    
#i've messed up math somehow, i'll get back to this
#honestly i feel like i've cheated cuz i just used the built-in multiplication function instead of writing my own
#i'll get to this tomorrow brain willing