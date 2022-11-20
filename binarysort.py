unsorted = [5, 9, 6, 8, 2]
max = len(unsorted)

x = 1
while x < max:
    if unsorted[x] > unsorted[x-1]:
        temp =unsorted[x]
        unsorted[x] = unsorted[x-1]
        unsorted[x-1] = temp
        print(unsorted)
    x+=1
print(unsorted)
