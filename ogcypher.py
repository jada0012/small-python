import string

def cypher(message):
    encoded = ''
    alphabet = list(string.ascii_lowercase)
    for i in message.lower():
        num = alphabet.index(i)
        encoded +=alphabet[num+1]
    return encoded

print(cypher('the quock roew'))