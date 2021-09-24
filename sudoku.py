from __future__ import nested_scopes
import random
import pyinputplus as pyin
board2 = [[i for i in range(9)] for j in range(3)]
board = [i for i in range(9)]


nb2 = [random.sample(board, len(board)) for board in board2]
nb = random.sample(board, len(board))
splits = [nb[i:1+3] for i in range(0, len(nb), 3)]
print(splits)
# print('this list contains elements from 1 to 3. enter the missing one')

# for i in range(random.randint(1, 3)):
#     nb[random.randint(0, len(board)-1)] = "_"
# print(nb)
# num_blank = nb.count("_")
# print(f'there are {nb.count("_")} missing numbers here')
# missing_num = pyin.inputInt("enter the missing number ")

# for i in range(num_blank):
#     while missing_num in nb:
#         print("wrong!")
#         missing_num = pyin.inputInt("enter the missing number ")

#         if missing_num not in nb:
#             print("correct!")
#             break


#     nb[nb.index("_")] = missing_num

#     print(nb)
