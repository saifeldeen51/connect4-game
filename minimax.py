from board import *
from random import shuffle

def MiniMax(board, depth, player):
    # get array of possible moves
    validMoves = getValidMoves(board)
    shuffle(validMoves)
    bestMove = validMoves[0]
    bestScore = float("-inf")

    if player == AI_PLAYER:
        opponent = HUMAN_PLAYER
    else:
        opponent = AI_PLAYER

    for move in validMoves:
        tempBoard = makeMove(board, move, player)[0]
        boardScore = minimize(tempBoard, depth - 1, player, opponent)
        if boardScore > bestScore:
            bestScore = boardScore
            bestMove = move
    return bestMove

def minimize(board, depth, player, opponent):
    validMoves = []
    for col in range(7):
        if isValidMove(col, board):
            temp = makeMove(board, col, player)[2]
            validMoves.append(temp)

    if depth == 0 or len(validMoves) == 0 or gameIsOver(board):
        return utilityValue(board, player)

    bestScore = float("inf")

    for move in validMoves:
        tempBoard = makeMove(board, move, opponent)[0]
        boardScore = maximize(tempBoard, depth - 1, player, opponent)
        if boardScore < bestScore:
            bestScore = boardScore
    return bestScore

def maximize(board, depth, player, opponent):
    validMoves = []
    for col in range(7):
        if isValidMove(col, board):
            temp = makeMove(board, col, player)[2]
            validMoves.append(temp)

    if depth == 0 or len(validMoves) == 0 or gameIsOver(board):
        return utilityValue(board, player)

    bestScore = float("-inf")

    for move in validMoves:
        tempBoard = makeMove(board, move, player)[0]
        boardScore = minimize(tempBoard, depth - 1, player, opponent)
        if boardScore > bestScore:
            bestScore = boardScore
    return bestScore
