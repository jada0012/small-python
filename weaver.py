import pathlib
from collections import defaultdict
from telnetlib import WONT

DICT_PATH = pathlib.Path('C:/Users/bobei/downloads/12dicts-6.0.2/International/2of4brif.txt')

with open(DICT_PATH) as f:
    dictionary = set(i.rstrip().lower() for i in f)
   
def wildcard(word, index):
    return f'{word[:index]}?{word[index+1:]}'

def allwildcards(word):
    wildcard_list = []
    for i in range(len(word)):
        wildcard_list.append(wildcard(word, i))
    return wildcard_list


start_word = 'trap'
end_word = 'door'

index = defaultdict(list)

for word in dictionary:
    for w in allwildcards(word):
        index[w].append(word)

def near_words(word):
    ret = []
    for i in allwildcards(word):
        ret += index[i]
    return set(ret)
print(near_words(start_word))

for i in near_words(start_word):
    print(f'words near to {i} are {near_words(i)}' )
#i am one recursive function away from completion i just need to turn my brain on