theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) 
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']) 
    print('-+-+-')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R']) 
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + ' which move? ')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)