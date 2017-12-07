#Christopher Holmes
#CST 205 Final

from random import randint
from __builtin__ import True



gameBoard = []
answer = []
boardSize = 4
pieces = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
backOfCards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
coordinates = {'A': (0, 0), 'B': (1,0), 'C': (2, 0), 'D': (3,0), 'E': (0,1), 'F': (1,1), 'G':(2,1), 'H': (3,1), 'I': (0,2), 'J': (1,2), 'K': (2,2), 'L': (3,2), 'M': (0,3), 'N': (1,3), 'O': (2,3), 'P': (3,3)}
won = False
numMatches = 0


def initializeGameBoard(board):
    cardNum = 0
    for i in range(boardSize):
        board.append([])
    for y in board:
        for x in range(boardSize):
            y.append(backOfCards[cardNum])
            cardNum += 1
            
def initializeAnswerBoard(board):
    for i in range(boardSize):
        board.append([])
    for y in board:
        for x in range(boardSize):
            index = randint(0, len(pieces)-1)
            y.append(pieces[index])
            del[pieces[index]]
            
def printBoard(board):
    for l in board:
        for e in l:
            print e,
        print
        
def printBoardGuess(gBoard, aBoard, firstX, firstY, secondX, secondY):
    for y in range(len(gBoard)):
        for x in range(len(gBoard)):
            if (y == firstY or y == secondY) and (x == firstX or x == secondX):
                if y == firstY and x == firstX:
                    print aBoard[firstY][firstX],
                elif y == secondY and x == secondX:
                    print aBoard[secondY][secondX],
                else:
                    print gBoard[y][x], 
            else:
                print gBoard[y][x],
        print
        
def returnCoordinates(card):
    if card == 'A':        
        return coordinates['A']
    elif card == 'B':
        return coordinates['B']
    elif card == 'C':
        return coordinates['C']
    elif card == 'D':
        return coordinates['D']
    elif card == 'E':
        return coordinates['E']
    elif card == 'F':
        return coordinates['F']
    elif card == 'G':
        return coordinates['G']
    elif card == 'H':
        return coordinates['H']
    elif card == 'I':
        return coordinates['I']
    elif card == 'J':
        return coordinates['J']
    elif card == 'K':
        return coordinates['K']
    elif card == 'L':
        return coordinates['L']
    elif card == 'M':
        return coordinates['M']
    elif card == 'N':
        return coordinates['N']
    elif card == 'O':
        return coordinates['O']
        
    
      

def checkGuess(firstX, firstY, secondX, secondY):
    if answer[firstY][firstX] == answer[secondY][secondX]:
        gameBoard[firstY][firstX] = answer[firstY][firstX]
        gameBoard[secondY][secondX] = answer[secondY][secondX]
        return True
    else:
        False  
        
initializeGameBoard(gameBoard)
initializeAnswerBoard(answer)
printBoard(gameBoard)
#printBoard(answer)

while not won:
    guess1Already = True
    guess2Already = True
    while guess1Already:
        guess1 = raw_input("Enter the letter of the first guess: ").upper()
        if gameBoard[returnCoordinates(guess1)[1]][returnCoordinates(guess1)[0]] in pieces:
            print("You already matched that square, %s. Try again")%guess1
            guess1Already = True
        else:
            break
    while guess2Already:
        guess2 = raw_input("Enter the letter of the second guess: ").upper()
        if gameBoard[returnCoordinates(guess2)[1]][returnCoordinates(guess2)[0]] in pieces:
            print("You already matched that square, %s. Try again")%guess2
            guess2Already = True
        else:
            break
    if checkGuess(returnCoordinates(guess1)[0], returnCoordinates(guess1)[1], returnCoordinates(guess2)[0], returnCoordinates(guess2)[1]):
        print("Match Found!")
        numMatches += 1
        if numMatches == 8:
            print("Congrats, you won!")
            won = True
        printBoard(gameBoard)
    else:
        print("No match, try again.")
        printBoardGuess(gameBoard, answer, returnCoordinates(guess1)[0], returnCoordinates(guess1)[1], returnCoordinates(guess2)[0], returnCoordinates(guess2)[1])
        