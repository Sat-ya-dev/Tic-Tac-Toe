def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3]) # printing the 1st row of board
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6]) # printing the 2nd row of board
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9]) # printing the 3rd row of board
    print("\n")


def spaceIsFree(position): # for checking whether the position is free or not
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position): # inserting "X" or 'O' in position in board
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
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


def checkForWin(): #winning conditions
    if board[1] == board[2] == board[3] and board[1] != ' ': # horizontal line
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ': # vertical line
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] == board[9] and board[1] != ' ': # diagonal line
        return True
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def WinPlayer(mark): # which player won
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


def checkDraw(): # checking for a draw when all the positions are occupied
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position) # player has been given letter 'O'
    return


def compMove():  #computer's move
    global num_leaves,max_depth
    bestScore = -1000
    bestMove = 0
    depth=1
    max_depth=1
    num_leaves=0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot   # assigning it to 'X'
            score = minimax(board, depth, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    print("The maximum depth is : ",max_depth)
    print("The number of leaves explored are :",num_leaves)
    print("\n")
    return


def minimax(board, depth, isMaximizing):
    global max_depth,num_leaves
    depth +=1
    if WinPlayer(bot):
        num_leaves += 1
        return 1
    elif WinPlayer(player):
        num_leaves += 1
        return -1
    elif checkDraw():
        num_leaves += 1
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth , False)
                max_depth = max(max_depth, depth)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth , True)
                max_depth = max(max_depth, depth)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("The board configuration is: ")
print(1,'|',2 ,'|',3)
print('--+---+--')
print(4, '|' ,5, '|' ,6)
print('--+---+--')
print(7, '|' ,8, '|' ,9)
print("\n")
player = 'O'
bot = 'X'

while not checkForWin() and not checkDraw():
    playerMove()
    if not checkForWin() and not checkDraw():
        compMove()