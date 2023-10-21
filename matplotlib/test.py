import csv
file = open("small-python/matplotlib/gas_prices.csv", "r")
data_reader = csv.reader(file)
for i in data_reader:
    print(i)