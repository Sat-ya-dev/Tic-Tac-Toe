def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])  # printing the 1st row of board
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])  # printing the 2nd row of board
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])  # printing the 3rd row of board
    print("\n")


def spaceIsFree(position):  # for checking whether the position is free or not
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):  # inserting "X" or 'O' in position in board
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():  # winning conditions
    if board[1] == board[2] == board[3] and board[1] != ' ':  # horizontal line
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':  # vertical line
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] == board[9] and board[1] != ' ':  # diagonal line
        return True
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def WinPlayer(mark):  # which player won
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] == board[3] and board[7] == mark:
        return True
    else:
        return False


def checkDraw():  # checking for a draw when all the positions are occupied
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)  # player has been given letter 'O'
    return


def compMove():  # uses the Minimax algorithm to determine the best move for the computer.
    # It assigns a score to each possible move and selects the move with the highest score.
    global NM_leaves, MX_depth
    bestScore = -1000
    bestMove = 0
    depth = 1
    MX_depth = 1
    NM_leaves = 0
    alpha = -999
    beta = 999

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot  # assigning it to 'X'
            score = minimax(board, depth, False, alpha, beta)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    print("the maximum depth is : ", MX_depth)
    print("The number of leaves explored are :", NM_leaves)
    print("\n")
    return


# define the function to implement the minimax algorithm with alpha-beta pruning
def minimax(board, depth, isMaximizing, alpha, beta):
    global MX_depth, NM_leaves
    depth += 1
    # check if a player has won, if so, return the corresponding score
    if WinPlayer(bot):
        NM_leaves += 1
        return 1
    elif WinPlayer(player):
        NM_leaves += 1
        return -1
    # check for a draw
    elif checkDraw():
        NM_leaves += 1
        return 0

    # if it's the maximizing player's turn
    if isMaximizing:
        bestScore = -1000
        # loop through each possible move
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                # recursively call minimax on the updated board
                score = minimax(board, depth, False, alpha, beta)
                MX_depth = max(MX_depth, depth)
                board[key] = ' '
                # update the best score if necessary
                if score > bestScore:
                    bestScore = score
                # update the alpha value
                alpha = max(alpha, bestScore)
                # check if pruning is possible
                # if MX_depth
                if alpha >= beta:
                    break
        return bestScore
    # if it's the minimizing player's turn
    else:
        bestScore = 1000
        # loop through each possible move
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                # recursively call minimax on the updated board
                score = minimax(board, depth, True, alpha, beta)
                MX_depth = max(MX_depth, depth)
                board[key] = ' '
                # update the best score if necessary
                if score < bestScore:
                    bestScore = score
                # update the beta value
                beta = min(beta, bestScore)
                # check if pruning is possible
                if alpha >= beta:
                    break
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("The board configuration is: ")
print(1, '|', 2, '|', 3)
print('--+---+--')
print(4, '|', 5, '|', 6)
print('--+---+--')
print(7, '|', 8, '|', 9)
print("\n")
player = 'O'
bot = 'X'

while not checkForWin() and not checkDraw():
    playerMove()
    if not checkForWin() and not checkDraw():
        compMove()