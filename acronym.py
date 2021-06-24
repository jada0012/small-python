

def acronym(words):
    acronyms = ''
    word1 = words.split()
    for i in word1:
        first_letter = i[0]
        acronyms += first_letter
    return acronyms


print(acronym('the lazy bum'))