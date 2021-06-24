ciphertext = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'

cipherlist = list(ciphertext.split())

col = 4
row = 5
plaintext = ''
start = 0
stop = row
key = '-1 2 -3 4'
translation_matriz = [None] * col 

keyint = [int(i) for i in key.split()]

for i in keyint:
    if i < 0:
        col_items = cipherlist[start: stop]
    elif i > 0: 
        col_items = cipherlist[stop:start]
    translation_matriz[abs(i) -1] = col_items
    start += row
    stop += row

for i in range(row):
    word = str(col_items.pop())
    plaintext += word + ''

print(f'plaintext = {plaintext}')