from minimaxAlphaBeta import *
from minimax import *
import time

RED     = '\033[1;31;40m'
YELLOW  = '\033[1;33;40m'
BLUE    = '\033[1;34;40m'
MAGENTA = '\033[1;35;40m'
CYAN    = '\033[1;36;40m'
WHITE   = '\033[1;37;40m'

dir_path = os.getcwd()
os.chdir(dir_path)

running_time_minimax = 0
running_time_alpha = 0
minimax_time = []
alpha_time = []

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

            init_time_minimax = time.time()

            board, aiFourInRow2 = ai2Turn(board,depth)
            running_time_minimax = time.time() - init_time_minimax
            minimax_time.append(running_time_minimax)
            print("             Minimax running time: %.4f seconds" % running_time_minimax)

            if aiFourInRow2:
                whileCondition = ai2Wins(board)
                if whileCondition ==0:
                    break

            #AI
            init_time_alpha = time.time()

            board, aiFourInRow = aiTurn(board,depth)
            running_time_alpha = time.time() - init_time_alpha
            alpha_time.append(running_time_alpha)
            print("             Alpha-Beta running time: %.4f seconds" % running_time_alpha)            
            if aiFourInRow:
                whileCondition = aiWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)
        else:
            #AI
            init_time_alpha = time.time()

            board, aiFourInRow = aiTurn(board,depth)
            running_time_alpha = time.time() - init_time_alpha
            alpha_time.append(running_time_alpha)   
            print("             Alpha-Beta running time: %.4f seconds" % running_time_alpha)
                     
            if aiFourInRow:
                whileCondition = aiWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)
            
            #Human
            init_time_minimax = time.time()
            board, aiFourInRow2 = ai2Turn(board,depth)
            running_time_minimax = time.time() - init_time_minimax
            minimax_time.append(running_time_minimax)
            print("             Minimax running time: %.4f seconds" % running_time_minimax)

            if aiFourInRow2:
                whileCondition = ai2Wins(board)

                if whileCondition ==0:
                    break
            printBoard(board)
    
mainFucntion()
