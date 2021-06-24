import xlsxwriter as xl

with open ('/home/jada/Documents/python/small-python-projects/spanish/ohyh.txt', encoding="UTF-8") as o:
    line1 = [line.rstrip().lstrip().split(':') for line in o]
row = 0
col = 0

workbook = xl.Workbook("vocabulatoryver.xlsx")
worksheet = workbook.add_worksheet()

for i in line1:
    worksheet.write(row, col, i[0])
    worksheet.write(row, col+1, i[1])
    row+=1
    

workbook.close()