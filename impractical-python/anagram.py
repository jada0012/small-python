from collections import Counter
import sys
import dictionary as d 


words = (d.dictionary('C:\\Users\\bobei\\Downloads\\12dicts-6.0.2\\International\\2of4brif.txt'))
words.append('a')#added a and i because some dictionaries don't have them
words.append('i')
words = sorted(words)

ini_name = input('Enter your name')

def anagramfinder(name, wordlist): #this finds the anagram from the name
    name_map = Counter(name) #makes a dictionary thingy with each letter and the number of times it occurs
    anagrams = []
    for word in wordlist: #from dictionary file
        test = ''
        word_map = Counter(word)
        for letter in word:
            if word_map[letter] <= name_map[letter]:#for each letter in the word, if it occurs less than or equal to the amount of times it does in the name, then it can be valid
                test += letter
        if Counter(test) == word_map:#if the test dictionary is the same as the original word, then it's a good anagram and gets added to the list
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print(f'remaining letters: = {name}')
    print(f'Letters left= {len(name)}')
    print(f'Number of anagrams left ={len(anagrams)}')

def choice(name): #takes user's word choice then checks it against the letters left in the name variable and gives you any leftover letters
    while True:

        choice = input("make a choice else Enter to restart or # to end")
        if choice =='':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split()) #adds all the letters in choice to candidate
        leftovers = list(name)

        for letter in candidate:
            if letter in leftovers:
                leftovers.remove(letter)#removes letter if it is in the choice, leaving only the ones that aren't yet used.
        if len(name) - len(leftovers) == len(candidate): #determines that the user didn't enter a word that's not in the list and is too long
            break
        else:
            print("won't work, choose again")
    name = ''.join(leftovers) #makes the new name the list of letters left over
    return choice, name

def main():
    name = ''.join(ini_name.lower().split()) #makes name ininame,lowercases it, and replaces spaces with hyphens
    name = name.replace('-', '')
    limit = len(name) #tells us how many letters are in the name and when to stop
    phrase = ''
    running = True
    while running:
        temphrase = phrase.replace(' ', '')#removes all the spaces in phrase
        if len(temphrase) < limit:
            print(f'Length of anagram: {len(temphrase)}') #shows the length of the anagram if it's under the limit

            anagramfinder(name, words)
            print(f'Anagram of name: {phrase}')#calls the anagram finder and gives possible phrases

            choose, name = choice(name) #adds the user's choice to the  thingy
            phrase += choose +' '#adds a space
        elif len(temphrase) == limit: #what happens when it reaches the limit
            print('it is finished, it is done, absalom')
            print(f'anagram of phrase: {phrase}')
            print()

            tryagain = input('Try again? press enter else n to quit')
            if tryagain.lower == 'n':
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()