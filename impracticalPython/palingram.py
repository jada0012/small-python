def palindrome(file):
    palindrome_list = []
    with open(file) as f:
        words = [i.rstrip().lower() for i in f]

    for word in words:
        if word[:] == word[::-1]:
            palindrome_list.append(word)
    return palindrome_list

print(palindrome('C:\\Users\\bobei\\Downloads\\12dicts-6.0.2\\International\\2of4brif.txt'))