
print('''
    Welcome to Tic Tac Toe!
    ''')
p1Mark = None
p2Mark = None
legitChecker = None
checker = ['X', 'O']
readyInput = None
readyInputArr = ['y', 'yes', 'ye', 'yeah']
playersandMarker = {'Player1': p1Mark, 'Player2': p2Mark}
gameEnd = False
vertical = False 
horizontal = False 
diagonal = False
board = [" " for x in range(0,9)]
currentPlayer = 'Player1'

def displayBoard(board):
    print(f'''
    {board[6]}|{board[7]}|{board[8]}
    {board[3]}|{board[4]}|{board[5]}
    {board[0]}|{board[1]}|{board[2]}
    
    ''')

def checkEnd(board,mark):
        return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
                (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
                (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
                (board[6] == mark and board[3] == mark and board[0] == mark) or # down the left
                (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
                (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
                (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
                (board[0] == mark and board[4] == mark and board[8] == mark)) # diagonal



while not legitChecker:
    print(''' Please Select 'X' or 'O' ''')
    p1Mark = input().upper()
    print('P1 MARKER', p1Mark)
    if p1Mark in checker:
        legitChecker = True 
        if p1Mark == 'X':
            playersandMarker['Player1'] = p1Mark 
            playersandMarker['Player2'] = 'O'
        else:
            playersandMarker['Player1'] = p1Mark 
            playersandMarker['Player2'] = 'X'

print('This is our Marker', playersandMarker)

print('''
    Are you ready to play? Enter Yes or No.
''')
readyInput = input().lower()


while not readyInput in readyInputArr:
    print('I will be here, please enter (y, ye, yes or yeah) when you are ready!')
    readyInput = input().lower()

while not gameEnd:
    if checkEnd(board,playersandMarker[currentPlayer]):  
        gameEnd = True    
        print(f'GAME OVER winner is {currentPlayer}',board)
    else: 
        validPositon = False 
        while not validPositon:
            position = int(input(f'{currentPlayer} : Enter Your Position'))
            if board[position] == ' ':
                board[position] = playersandMarker[currentPlayer]
                if currentPlayer == 'Player1':
                    currentPlayer = 'Player2'
                else:
                    currentPlayer = 'Player1'
                displayBoard(board)
                validPositon = True
            
            else:
                displayBoard(board)
                print('Its already occupied, Please Select other postion')

    
           

