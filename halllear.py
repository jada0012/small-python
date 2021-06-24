import sys
name_1 = sys.stdin.readline().rstrip()

capital_count = 0
unique_letters = 0
words = 0
namenospace = ""
i = name_1.split()
len_tot = 0
for g in i:
  len1 = len(g)
  len_tot += len1
  words += 1
  namenospace+=g


name2 = namenospace.lower().rstrip()

s = set(name2)
for i in name_1:
  if i.isupper() == True:
    capital_count+=1


print(len_tot)
print(words)
print(capital_count)
print(len(s))
print(name_1[::-1])
# # import sys
# # binary = sys.stdin.readline().rstrip()
# # new_bin = ""

# # for i in binary:
# #   if i == "0":
# #     new_bin += "1"
# #   elif i == "1":
# #     new_bin += "0"

# # binary_num = "0b" + new_bin
# # binary_2 = "0b1"
# # integer_sum = int(binary_num, 2) + int(binary_2, 2)
# # binary_sum = bin(integer_sum)
# # print(new_bin)

# # print(new_bin[2:])

# import sys
# import math


# numbers = sys.stdin.readline().rstrip()
# num_list = numbers.split()
# int_num_list = []
# product1 = 1
# product2 = 1
# product3 = 1
# products = []

# turnip_box = [0.5, 0.8, 0.4]


# for i in num_list:
#   int_num_list.append(float(i))


# for i in range(3):
#   product1 *= math.floor(int_num_list[i]/turnip_box[i])
#   products.append(product1)
# int_num_list.append(int_num_list[0])
# del int_num_list[0]

# for i in range(3):
#   product2*= math.floor(int_num_list[i]/turnip_box[i])
#   products.append(product2)


# int_num_list.append(int_num_list[0])
# del int_num_list[0]

# for i in range(3):
#   product3 *= math.floor(int_num_list[i]/turnip_box[i])
#   products.append(product3)

  




# maxi = max(products)
# print(maxi)
# import sys
# array = []
# num_parts = int(sys.stdin.readline())

# battery_cap = 0

# for i in range(num_parts):
#   inputs = sys.stdin.readline().lstrip().rstrip()
#   print(inputs)
#   splited = inputs.split(",")
#   temp_list = []
#   for i in splited:
#     temp_list.append(int(i))
#   array.append(temp_list)

  
# for leg in array:
#   if leg[1] == 0:
#     battery_cap += leg[0]
#   elif leg[1] > 0:
   
#     battery_cap+= leg[0] + (leg[1] //10)
#   elif leg[1] < 0:
#     battery_cap -= leg[1] //10 
#   print(f"{battery_cap=}")
  



# )
 

# print(battery_cap)

# import sys

# num_cand = int(sys.stdin.readline())
# num_voter = int(sys.stdin.readline())
# pref_list = []
# votes_1 = 0
# votes_2 = 0
# votes_3 = 0
# votes_4 = 0
# votes_5 = 0

# for i in range(num_voter):
#   pref_str = sys.stdin.readline().rstrip().split()
#   pref_map = map(int, pref_str)
#   listy = list(pref_map)
#   pref_list.append(listy)
  
# for vote in pref_list:
#   print(vote)

# import sys
# import sys
# import sys

# numbers = sys.stdin.readline().rstrip().split()
# temp_num = map(int, numbers)
# num_list = list(temp_num)
# coords_lst = []
# print(num_list)

# for i in range(num_list[0]):
#   coords = sys.stdin.readline().rstrip()
#   coords_lst.append(coords)

# for i in coords_lst:
#   print(i[0])

import sys

