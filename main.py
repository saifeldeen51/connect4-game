from minimaxAlphaBeta import *
from minimax import *

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




def aiTurn(board,depth):
    aiMove  = MiniMaxAlphaBeta(board, depth, AI_PLAYER)
    board = makeMove(board, aiMove, AI_PLAYER)[0]
    aiFourInRow  = findFours(board)

    return  board, aiFourInRow

def aiWins(board):
    printBoard(board)
    print('                     '+RED+"AI 1 WINS !!!!\n" +'\033[1;37;40m')
    playagain = True if input(YELLOW+'DO YOU WANT TO PLAY AGAIN(y/n)?'+WHITE).lower() == 'y' else False
    #saveBoard(board)
    if playagain:
        mainFucntion()
    return 0
def ai2Turn(board,depth):
    aiMove  = MiniMax(board, depth, HUMAN_PLAYER)
    board = makeMove(board, aiMove, HUMAN_PLAYER)[0]
    aiFourInRow2  = findFours(board)

    return  board, aiFourInRow2

def ai2Wins(board):
    printBoard(board)
    print('                     '+RED+"AI 2 WINS !!!!\n" +'\033[1;37;40m')
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

            board, aiFourInRow2 = ai2Turn(board,depth)
            if aiFourInRow2:
                whileCondition = ai2Wins(board)
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
            board, aiFourInRow2 = ai2Turn(board,depth)
            if aiFourInRow2:
                whileCondition = ai2Wins(board)

                if whileCondition ==0:
                    break
            printBoard(board)

mainFucntion()
