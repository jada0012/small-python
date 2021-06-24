import csv
import pyinputplus as pyin
rowlist = [["Day", "FSlur", "RSlur"], [1, 10, 15 ], [2, 2, 9], [3, 0, 7], [4, 4, 6], [5, 3, 5], [6, 1, 5], [7, 2, 3], [8, 0, 2], [9, 2, 4], [10, 0, 1], [11, 0, 3], [12, 5, 4], [13, 0, 2]]

day = rowlist[-1][0] + 1
Fslur = pyin.inputInt('How many F-s? ')
RSlur = pyin.inputInt('How many R-s? ')

rowlist.append([day, Fslur, RSlur])

# with open('D:\\python\\small-python-projects\\mpl_slur\\tallyval.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rowlist)
   

