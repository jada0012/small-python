def dictionary(file):
    with open(file) as f:
        words = [i.rstrip().lower() for i in f]
        return words
    

