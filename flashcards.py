with open ("/home/jada/Documents/python/small-python-projects/spanish/oheyah.txt", encoding='UTF-8') as f:
    questions = [line.rstrip().strip('-') for line in f]

print(questions)