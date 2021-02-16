import pyinputplus as pyin
numboard = [
    [[0,0], [2], [3]],
    [[4],[5], [6]],
    [[7], [8], [9]]
]
def ordering():
    for i in numboard:
        print(i)
    print('this is the numbering of the board. use these numbers to determine where you want to play')
board = [
    ['*', '*','* '],
    ['*', '*','* '],
    ['*', '*','* '],

]


def prettyboard(board):
    print(0,1,2)
    print('---------')
    for i in board:
        print('|', *i , end='')
        print('|')
        
    print('---------')
   
def movevalid(x,y):
    
    if board[x][y] =='*':
        return True
    else:
        print('invalid try again')
def movemaker(x, y, turn):

    

        board[x][y] = turn
    

def gameloop():
    count = 1
    turn = 'X'
    win = False
    while True:
        print(f'Turn number {count}, it is {turn} play')
        
        x = pyin.inputNum('Enter your x coordinate', min=0, max=2)
        y = pyin.inputNum('Enter your y coordinate', min=0, max=2)
        
        movemaker(x,y, turn)

        prettyboard(board)
        count += 1
        if turn == 'X':
            turn ='O'
        else:
            turn = 'X'
       
        if count >=5:
            if board[0][0] == board[0][1] == board[0][2] != '*' or board[1][0] == board[1][1] == board[1][2] != '*' or board[2][0] == board[2][1] == board[2][2] != '*'or board[0][0] == board[1][0]== board[2][0] != '*' or  board[0][1] == board[1][1] == board[2][1] != '*' or board[0][2] ==  board[1][2] ==  board[2][2]!= '*':
                print('there is a winner!')
                win = True
                print(win)
                
        if count > 9 or  win == True:
            playagain = pyin.inputYesNo('Do you want to play again?')
            if playagain == 'no':
                print('was a good game')
                break
            else:
                gameloop()


gameloop()