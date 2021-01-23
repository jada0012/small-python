#if word begins with consonant, remove consonant and add it to end of word with ay, if word begins with vowel, then add way to the end

def piglatin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if word[0] in vowels:
        return '%s-way'%(word)
    else:
        return '%s-%say'%(word[1:], word[0])
