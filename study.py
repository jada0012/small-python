import random
from itertools import combinations
import xlsxwriter as xl 
subjects = ['Lit', 'IT', 'Physics', 'Chemistry', 'Add Math', 'Math', 'Spanish', 'Econ']



stuff = list(combinations(subjects, 2))
stuffled = random.sample(stuff,k=len(stuff))


workbook =xl.Workbook('StudySchedule3.xlsx')
worksheet = workbook.add_worksheet()


schedule = (list((count, items)) for count, items in enumerate(stuffled, start=1))

row = 0
col = 0
for  day, subject in (schedule):
    worksheet.write(row, col, day)
    worksheet.write(row, col+1, str(subject))
    row+=1


workbook.close()

