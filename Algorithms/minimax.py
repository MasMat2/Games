
import time, copy
board = [[" " for j in range(3)] for i in range(3)]


def draw_board(board):
    print('  1   2   3')
    for line in range(3):
        if line != 0:
            print('----------')
        for value in range(3):
            if value == 0:
                print(line+1, end=' ')
            print(board[value][line], end='')
            if value != 2:
                print('', end=' |')
        print()
    print()

def winner(board, x, y):
    if (len(set([board[i][i] for i in range(3)])) == 1) and (board[0][0] != ' '):
        return board[0][0]
    if (len(set([board[2-i][i] for i in range(3)])) == 1) and (board[2][0] != ' '):
        return board[2][0]
    if (len(set(board[x])) == 1) and (board[x][0] != ' '):
        return board[x][0]
    if (len(set([board[j][y] for j in range(3)])) == 1) and (board[0][y] != ' '):
        return board[0][y]
    return None

def get_value(di, max=True):
    if max:
        current = -90
    else:
        current = 90
    for key in di.keys():
        if di[key] > current:
            if max:
                current = di[key]
                k = key
        else:
            if not max:
                current = di[key]
                k = key
    return k



def minimax(board, bo):
    if bo:
        results = {}
        for i in range(3):
            for j in range(3):
                board1 = copy.deepcopy(board)
                if board1[i][j] == ' ':
                    board1[i][j] = 'O' #
                    result = sum([1 for d in range(3) for e in range(3) if board1[d][e] == ' '])
                    if winner(board1, i, j) == 'O': #
                        return (i,j), result+1
                    elif result > 0:
                        k, v = minimax(board1, not bo)
                        results[(i,j)] = v
                    else:
                        results[(i,j)] = 0

        if len(results.keys()) > 0:
            key  = get_value(results, max=True) #
            return key, results[key]


    else:
        results = {}
        for i in range(3):
            for j in range(3):
                board1 = copy.deepcopy(board)
                if board1[i][j] == ' ':
                    board1[i][j] = 'X' #
                    result = sum([1 for d in range(3) for e in range(3) if board1[d][e] == ' '])
                    if winner(board1, i, j) == 'X': #
                        return (i,j), -result-1#
                    elif result > 0:
                        k, v = minimax(board1, not bo)
                        results[(i,j)] = v
                    else:
                        results[(i,j)] = 0
        if len(results.keys()) > 0:
            key  = get_value(results, max=False) #
            return key, results[key]

player_turn = True
draw_board(board)
while True:
    if player_turn:
        print('You are the X, Choose a coordinate')
        x,y = (int(i)-1 for i in input().split(','))
        board[x][y] = 'X'
        player_turn = not player_turn
        draw_board(board)
        winner1 = winner(board, x, y)
        if winner1:
            print(f'The winner is {winner1}')
            break
    else:
        time.sleep(0.25)
        print('It\'s the computer\'s turn')
        time.sleep(0.25)
        if sum([1 for d in range(3) for e in range(3) if board[d][e] == ' ']) == 8:
            if board[1][1] == " ":
                x,y = 1,1
            else:
                x,y = 0,0
        else:
            x, y = minimax(board, True)[0]
        board[x][y] = 'O'
        print(f'Computer chose ({x+1},{y+1})')
        player_turn = not player_turn
        draw_board(board)
        winner1 = winner(board, x, y)
        if winner1:
            print(f'The winner is {winner1}')
            break

draw_board(board)
