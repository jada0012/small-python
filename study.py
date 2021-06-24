import random
from itertools import combinations
import xlsxwriter as xl 
subjects = ['Eng', 'IT', 'Physics', 'Chemistry', 'Add Math', 'Math', 'Spanish', 'Econ']



stuff = list(combinations(subjects, 2))
stuffled = random.sample(stuff,k=len(stuff))


workbook =xl.Workbook('StudySchedule5.xlsx')
worksheet = workbook.add_worksheet()

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

schedule = (list((count, items)) for count, items in enumerate(stuffled, start=0))
for day, subject in schedule:
    print(day, subject)
row = 0
col = 0
# for  day, subject in (schedule):
#     worksheet.write(row, col, day)
#     worksheet.write(row, col+1, str(subject))
#     row+=1


# workbook.close()


    
    