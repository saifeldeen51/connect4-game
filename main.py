from minimaxAlphaBeta import *
from minimax import *
import time
from matplotlib import pyplot as plt


RED     = '\033[1;31;40m'
YELLOW  = '\033[1;33;40m'
BLUE    = '\033[1;34;40m'
MAGENTA = '\033[1;35;40m'
CYAN    = '\033[1;36;40m'
WHITE   = '\033[1;37;40m'

dir_path = os.getcwd()
os.chdir(dir_path)
# init_time_minimax = time.time()
# init_time_alpha = time.time()
running_time_minimax = 0
running_time_alpha = 0
minimax_time = []
alpha_time = []

def loadBoard():

    return None, False

def aiMinimaxTurn(board,depth):
    aiMove  = MiniMax(board, depth, O_PLAYER)
    board = makeMove(board, aiMove, O_PLAYER)[0]
    aiMinFourInRow  = findFours(board)

    return  board, aiMinFourInRow

def aiMininmaxWins(board):
    printBoard(board)
    print('                     '+RED+"AI agent with Minimax WINS !!!!\n" +'\033[1;37;40m')
    playagain = True if input(YELLOW+'DO YOU WANT TO PLAY AGAIN(y/n)?'+WHITE).lower() == 'y' else False
    #saveBoard(board)
    if playagain:
        mainFucntion()
    return 0

def aiAlphaTurn(board,depth):
    aiMove  = MiniMaxAlphaBeta(board, depth, X_PLAYER)
    board = makeMove(board, aiMove, X_PLAYER)[0]
    aiAlphaFourInRow  = findFours(board)

    return  board, aiAlphaFourInRow

def aiAlphaWins(board):
    printBoard(board)
    print('                     '+RED+"AI agent With Alpha-beta pruning WINS !!!!\n" +'\033[1;37;40m')
    playagain = True if input(YELLOW+'DO YOU WANT TO RESTART THE GAME(y/n)?'+WHITE).lower() == 'y' else False
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
        whomStart = True if input(YELLOW + 'DO YOU WANT THE AI AGENT WITH MINIMAX TO START(y/n)? ' + WHITE).lower() == 'y' else False
    if board == None:
        board = initializeBoard()

    while(whileCondition):
        # init_time_minimax = time.time()
        # init_time_alpha = time.time()
        if isBoardFilled(board) :
            print("GAME OVER\n")
            break

        if whomStart:
            #AI with mimimax algorithm
            init_time_minimax = time.time()
            board, aiMinFourInRow = aiMinimaxTurn(board,depth)
            running_time_minimax = time.time() - init_time_minimax
            minimax_time.append(running_time_minimax)
            print("             Minimax running time: %.4f seconds" % running_time_minimax)

            if aiMinFourInRow:
                whileCondition = aiMininmaxWins(board)
                if whileCondition ==0:
                    break

            #AI with Alpha-beta algorithm
            init_time_alpha = time.time() 
            board, aiAlphaFourInRow = aiAlphaTurn(board,depth)
            running_time_alpha = time.time() - init_time_alpha
            alpha_time.append(running_time_alpha)
            print("             Alpha-Beta running time: %.4f seconds" % running_time_alpha)            
            if aiAlphaFourInRow:
                whileCondition = aiAlphaWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)
        else:
            #AI with Alpha-beta algorithm
            init_time_alpha = time.time()
            board, aiAlphaFourInRow = aiAlphaTurn(board,depth)
            running_time_alpha = time.time() - init_time_alpha
            alpha_time.append(running_time_alpha)   
            print("             Alpha-Beta running time: %.4f seconds" % running_time_alpha)
                     
            if aiAlphaFourInRow:
                whileCondition = aiAlphaWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)
            
            #AI with mimimax algorithm
            init_time_minimax = time.time()
            board, aiMinFourInRow = aiMinimaxTurn(board,depth)
            running_time_minimax = time.time() - init_time_minimax
            minimax_time.append(running_time_minimax)
            print("             Minimax running time: %.4f seconds" % running_time_minimax)

            if aiMinFourInRow:
                whileCondition = aiMininmaxWins(board)

                if whileCondition ==0:
                    break
            printBoard(board)
    print()        
    print("maximum time of Minimax algorithm ---> ",max(minimax_time),"sec")
    print("minimun time of Minimax algorithm ---> ",min(minimax_time),"sec") 
    print()
    print("-------------------------------------------------------------------------------") 
    print()
    print("maximum time of Alpha-Beta algorithm ---> ",max(alpha_time),"sec")  
    print("minimum time of Alpha-Beta algorithm ---> ",min(alpha_time),"sec") 
    print()                 
    plt.title("Speed Performance For Two Algorithms")
    plt.ylabel("Time (seconds)")
    plt.xlabel("Round")
    plt.plot(minimax_time, color = "red", label = "Minimax")
    plt.plot(alpha_time, color = "blue", label = "Alpha-Beta")
    plt.legend()
    plt.show()    
    
mainFucntion()
