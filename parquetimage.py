import random
import csv
import pandas as pd
questions = ['what is the net worth?', 'what is the gross worth?', 'what is the vat due?']
answers = ['the net worth is ', 'the gross worth is ', 'the vat due is ']

# with open("metadata2.txt", "w") as f:
#     f.write("file_name,question\n")
#     for i in range(423):
#         index = random.randint(0,len(questions)-1)
#         f.write(f"{i}.png,{questions[index]}\n")

# with open("pleasegod.csv", 'w', newline='') as file:
#     for i in range(423):
#         writer = csv.writer(file)
#         writer.writerow(['file_name', 'question'])
#         writer.writerow([f"{i}.png", f"{questions[0]}"])

read_file = pd.read_csv(r"C:\Users\bobei\python\small-python\metadata.txt")
read_file.to_csv(r"C:\Users\bobei\python\small-python\train\metadata2.csv", index=False)

# import pyarrow.parquet as pq

# index = 0
# table = pq.read_table(r"C:\Users\bobei\Downloads\train-00000-of-00001-a5c51039eab2980a.parquet")
# for img in table['image']:
#     b = img['bytes'].as_py()
#     with open(f'train/{index}.png', 'wb') as f:
#         f.write(b)
#         index+=1