from minimaxAlphaBeta import *

RED     = '\033[1;31;40m'
YELLOW  = '\033[1;33;40m'
BLUE    = '\033[1;34;40m'
MAGENTA = '\033[1;35;40m'
CYAN    = '\033[1;36;40m'
WHITE   = '\033[1;37;40m'

dir_path = os.getcwd()
os.chdir(dir_path)


def loadBoard():

    return None, False


def playerTurn(board):
    Col = input(YELLOW + 'Choose a Column between 1 and 7: ' + WHITE)
    if not(Col.isdigit()):
        print(MAGENTA + "Input must be integer!" + WHITE)
        return playerTurn(board)

    playerMove = int(Col) - 1

    if playerMove < 0 or playerMove > 6:
        print(MAGENTA + "Column must be between 1 and 7!" + WHITE)
        return playerTurn(board)

    if not(isColumnValid(board, playerMove)):
        print(MAGENTA + "The Column you select is full!" + WHITE)
        return playerTurn(board)


    board = makeMove(board, playerMove, HUMAN_PLAYER)[0]
    playerFourInRow  = findFours(board)
    return board, playerFourInRow

def playerWins(board):
    printBoard(board)
    print('                    '+BLUE+"HUMAN WINS !!\n" +WHITE)
    playagain = True if input(YELLOW +'DO YOU WANT TO PLAY AGAIN(y/n)?'+WHITE).lower() == 'y' else False
    #saveBoard(board)
    if playagain:
        mainFucntion()
    return 0

def aiTurn(board,depth):
    aiMove  = MiniMaxAlphaBeta(board, depth, AI_PLAYER)
    board = makeMove(board, aiMove, AI_PLAYER)[0]
    aiFourInRow  = findFours(board)

    return  board, aiFourInRow

def aiWins(board):
    printBoard(board)
    print('                     '+RED+"AI WINS !!!!\n" +'\033[1;37;40m')
    playagain = True if input(YELLOW+'DO YOU WANT TO PLAY AGAIN(y/n)?'+WHITE).lower() == 'y' else False
    #saveBoard(board)
    if playagain:
        mainFucntion()
    return 0


def getDepth():
    depth = input(YELLOW + 'ENTER DIFFICULTY(1-5): ' + WHITE)
    if not(depth.isdigit()):
        print(MAGENTA + 'Input must be integer!' + WHITE)
        return getDepth()

    depth = int(depth,10) 

    if depth < 1 or depth > 5:
        print(MAGENTA + "Difficulty must be between 1 and 5!" + WHITE)
        return getDepth()

    return depth

def mainFucntion():
    #board = initializeBoard()
    os.system('cls' if os.name == 'nt' else 'clear')
    board, loadFlag = loadBoard()
    if board == None:
        board = initializeBoard()
    printBoard(board)
    depth = getDepth()
    whileCondition = 1
    if loadFlag == True:
        whomStart = True
    else:
        whomStart = True if input(YELLOW + 'DO YOU WANT TO START(y/n)? ' + WHITE).lower() == 'y' else False
    if board == None:
        board = initializeBoard()

    while(whileCondition):
        if isBoardFilled(board) :
            print("GAME OVER\n")
            break

        if whomStart:

            board, playerFourInRow = playerTurn(board)
            if playerFourInRow:
                whileCondition = playerWins(board)
                if whileCondition ==0:
                    break

            #AI
            board, aiFourInRow = aiTurn(board,depth)
            if aiFourInRow:
                whileCondition = aiWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)
        else:
            #AI
            board, aiFourInRow = aiTurn(board,depth)
            if aiFourInRow:
                whileCondition = aiWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)
            
            #Human
            board, playerFourInRow = playerTurn(board)
            if playerFourInRow:
                whileCondition = playerWins(board)

                if whileCondition ==0:
                    break

            printBoard(board)

mainFucntion()
