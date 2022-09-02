import pathlib
from collections import defaultdict

DICT_PATH = pathlib.Path('C:/Users/bobei/downloads/12dicts-6.0.2/International/2of4brif.txt')

with open(DICT_PATH) as f:
    dictionary = set(i.rstrip().lower() for i in f)
with open('otherwords.txt') as g:
    morewords = set(i.rstrip().lower() for i in g)
dictionary = list(dictionary) + list(morewords)
dictionary = set(dictionary)
def wildcard(word, index):
    return f'{word[:index]}?{word[index+1:]}'

def allwildcards(word):
    wildcard_list = []
    for i in range(len(word)):
        wildcard_list.append(wildcard(word, i))
    return wildcard_list


start_word = 'wham'
end_word = 'boom'

index = defaultdict(list)

for word in dictionary:
    for w in allwildcards(word):
        index[w].append(word)

# def near_words(start_word, end_word, num=1, path=[]):
# # def near_words(start_word, end_word, num=1):
#     ret = []
#     if num > 10:
#         print('stop for now!')
#         return "biu"
#     else:
#         for i in allwildcards(start_word):
#             ret += set(index[i])

        

#         ret = sorted(list(set(ret)))
#         ret.pop(ret.index(start_word))
#         print(f"iteration number {num}")
#         num+=1
#         path.append(ret[0])
#         print(f"{start_word=}, similar words are: {ret}, path so far is {path}")
#         print(f"{start_word=}, similar words are: {ret}")

#         # for i in range(len(ret)-1):
#         #     near_words(ret[i], end_word, num)
#         near_words(ret[0], end_word, num, path)
def near_words(start_word):
# def near_words(start_word, end_word, num=1):
    ret = []
   

    for i in allwildcards(start_word):
        ret += set(index[i])
        ret = sorted(list(set(ret)))
        ret.pop(ret.index(start_word))
        return ret
 
   
       
print(near_words('chat'))



# i am one recursive function away from completion i just need to turn my brain on
# pseud