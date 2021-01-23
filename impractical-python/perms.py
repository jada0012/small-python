from itertools import permutations
name = 'jurne'
perms = [''.join(i) for i in permutations(name)]


def cvmap(name):
    vowels = 'aeiouy'
    temp = ''
    for i in name:
        
        if i in vowels:
            temp += 'v'
        else:
            temp += 'c'
    return temp
    
print(cvmap('jorernnnweorereeee'))