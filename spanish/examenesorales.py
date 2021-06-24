import random
from itertools import combinations
import xlsxwriter as xl 

with open ("/home/jada/Documents/python/small-python-projects/spanish/orals.txt", encoding="UTF-8") as o:
    questions = [line.rstrip() for line in o]


workbook = xl.Workbook("orals302.xlsx")
worksheet = workbook.add_worksheet()

row = 0
col = 0

for i in questions:
    worksheet.write(row, col, i)
    worksheet.write(row, col+1, "think")
    row+=1

workbook.close()
