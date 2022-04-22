''' printBoard is taken verbatim from book '''

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def testWin(board):
    newset = [[] for x in range(6)]

    for space,move in board.items():
        if 'top' in space:
            newset[0].append(move)
        if 'mid' in space:
            newset[1].append(move)
        if 'low' in space:
            newset[2].append(move)
        if 'L' in space:
            newset[3].append(move)
        if 'M' in space:
            newset[4].append(move)
        if 'R' in space:
            newset[5].append(move)

    if board['top-L'] == board['mid-M'] and board['top-L'] == board['low-R'] and board['top-L'] != ' ':
        return True
    if board['low-L'] == board['mid-M'] and board['low-L'] == board['top-R'] and board['low-L'] != ' ':
        return True

    for set in newset:
        if set.count('x') == 3 or set.count('o') == 3:
            return True

    return False

NUM_MOVES = 9

player_move = ''
game_win = False
print('Let\'s play tic tac toe!')
printBoard(theBoard)

for turn in range(NUM_MOVES):
    if turn % 2 == 0:
        player_move = 'x'
    else:
        player_move = 'o'

    print(f'{player_move}\'s turn. Indicate space you\'d like place your character')
    # move = str(input('--->\t'))

    while True:
        move = str(input('--->\t'))
        if move not in theBoard:
            print('Please enter a valid space, such as "top-L", "mid-M", or "low-R"')
            continue
        elif move in theBoard and theBoard[move] != ' ':
            print('That space is already taken')
            continue
        else:
            break

    theBoard[move] = player_move
    printBoard(theBoard)
    print('')
    game_win = testWin(theBoard)

    if game_win:
        print(f'{player_move.capitalize()} Wins!')
        break

if not game_win:
    print('It\'s a draw')

