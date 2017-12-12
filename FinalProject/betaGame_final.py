# Michael Loeser
# John Seals
# Patrick Gonzales
# Christopher Holmes
# Christopher Buckey
# CST-205 Final Project
# Sound Byte Puzzle

#Final Project 

from random import *
import re
from __builtin__ import True
from time import sleep

#Set the directory that the project is running from to obtain all pictures automatically
showInformation("Please select the folder containing the scripts and game files.")
folder = pickAFolder()
setMediaFolder(folder)

##########
# Sound Puzzle variables

# edit for other applications!!!
soundFilePath = getMediaPath('werewolf.wav')

gameDesc = ('Welcome to the sound puzzle!\n'
            'To win you must put the snippets back in\n'
            'order to produce the original soundbyte.\n'
            'If you can do this within 4 tries you win!\n'
            'Fail and you are thrown out of the game!\n\n'
            'Click \'OK\' to hear the soundbyte and start the game.')

moveDesc = ('Select the number of the snippet to play that portion.\n\n'
            'Type "Play" to submit the spaces and soundbytes to see\n'
            '  if you have solved the puzzle.\n\n'
            'example: Play 2 4 1 3 5 6\n\n'
            'Type \'Exit\' to quit\n\n'
            '-- Please provide an action --')

tryAgainMessage = 'That is not correct.  Try again'

winMessage = 'Congratulations!\nYou put the pieces together\ncorrectly to WIN the game!\n\nEnjoy the full soundbyte.'
failMessage = 'We\'re sorry (not sorry).  You failed!'
invalidEntry = 'That is an invalid entry.  Try again'

maxAttempts = 4
numBytes = 6

debugFlag = false

##########
# Memory Game variables

gameBoard = []
answer = []
boardSize = 4
pieces = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

#Empty pictures that are used througout the game
gameBoardPic = makeEmptyPicture(400, 400)
tempGameBoardPic = makeEmptyPicture(400, 400)

#Load in all the pictures for the back of the cards
backA = makePicture(getMediaPath("A.png"))
backB = makePicture(getMediaPath("B.png"))
backC = makePicture(getMediaPath("C.png"))
backD = makePicture(getMediaPath("D.png"))
backE = makePicture(getMediaPath("E.png"))
backF = makePicture(getMediaPath("F.png"))
backG = makePicture(getMediaPath("G.png"))
backH = makePicture(getMediaPath("H.png"))
backI = makePicture(getMediaPath("I.png"))
backJ = makePicture(getMediaPath("J.png"))
backK = makePicture(getMediaPath("K.png"))
backL = makePicture(getMediaPath("L.png"))
backM = makePicture(getMediaPath("M.png"))
backN = makePicture(getMediaPath("N.png"))
backO = makePicture(getMediaPath("O.png"))
backP = makePicture(getMediaPath("P.png"))

#Generate dictionary associating letter with image file
backOfCards = {'A': backA, 'B': backB, 'C': backC, 'D': backD, 'E': backE, 'F': backF, 'G': backG, 'H': backH, 'I': backI, 'J': backJ, 'K': backK, 'L': backL, 'M': backM, 'N': backN, 'O': backO, 'P': backP}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
coordinates = {'A': (0, 0), 'B': (1,0), 'C': (2, 0), 'D': (3,0), 'E': (0,1), 'F': (1,1), 'G':(2,1), 'H': (3,1), 'I': (0,2), 'J': (1,2), 'K': (2,2), 'L': (3,2), 'M': (0,3), 'N': (1,3), 'O': (2,3), 'P': (3,3)}

#Load in all the images to use as game pieces
image1 = makePicture(getMediaPath("Image1.jpg"))
image2 = makePicture(getMediaPath("Image2.jpg"))
image3 = makePicture(getMediaPath("Image3.jpg"))
image4 = makePicture(getMediaPath("Image4.jpg"))
image5 = makePicture(getMediaPath("Image5.jpg"))
image6 = makePicture(getMediaPath("Image6.jpg"))
image7 = makePicture(getMediaPath("Image7.jpg"))
image8 = makePicture(getMediaPath("Image8.jpg"))

#Generate dictionaries for use
imageDict = {1: image1, 2: image2, 3: image3, 4: image4, 5: image5, 6: image6, 7: image7, 8: image8}

########

def betaGame():
  #variables
  solved1 = false
  solved2 = false
  solved3 = false
  solved4 = false
  
  solved1Display = ''
  solved2Display = ''
  solved3Display = ''
  solved4Display = ''
  
  play = true
  win = false

  # removed from line 2 to save space -- "You should never have signed up for a class this early." \
  #intro text
  intro = "A yawn so big it takes two hands to cover creeps across your weary face. You're in class again...this time it's dreadfully early in the morning. \n"  \
          "The clock on the wall by the door says '10:30', still a full 90 minutes left to go before " \
          "you can go snooze in the cafeteria. On the desk in front of you, there is a plastic, spiral bound textbook which looks suspiciously as if it did " \
          "not come from a professional printing company, rather it looks as if it were printed right here on campus. The title says: Biology, for CS Students. \n" \
          "You wonder what Biology has to do with Computer Science but since it's on your pre-reqs list, you're locked in for 4 hours of lecture per week. \n" \
          "Your professor is exuberant and you wish you could match her enthusiasm, but as you look outside you see the sunshine and begin to dream of warm, " \
          "sandy beaches far away... \n" \
          "\"What you want to do is put your hand inside the default constructor, then take your razor blade and make an incision so that the resulting torus " \
          "will be equidistant from the proximal disjunct.\"...your instructor says, calmly. \n" \
          "You shake yourself out of what would've been a beautiful reverie in order to take notes, but where's your farorite Snoopy pencil?  It must've fallen " \
          "off the desk.  You bend down to look underneath the desk but instead of a comical black and white pencil with a flying dog house on it, you find a " \
          "small, ancient electronic device with what looks like a mini computer screen.  Odd, it must've fallen out of the backpack of someone in the previous lecture. \n" \
          "It feels heavy, like one of those old hand held electronic games your grandpa was telling you about the other day.  The 'game lad' or something to that " \
          "effect, silly grandpa.  Good thing you didn't sit in the front row today.  There is a worn sticker on the bottom that says: \"Warning: Use of this device " \
          "as an improvised weapon may result in serious injury or death.  Calm down, the puzzles aren't that difficult.\" Despite your hesitance at this distraction, " \
          "you decide to throw caution to the wind and see if this thing really works. \n" \
          "The screen says: \n" \
          "Welcome to the Fabulous Betawares Puzzle Extravaganza. \n" \
          "Here you can explore puzzle games which will challenge your " \
          "mental dexterity and push your patience to the limit.  Solve " \
          "all the puzzles and guess what, YOU WIN!\n" \
          "Fail to solve all the puzzles and \'all your base are belong to us\'. \n\n" \
          "Have fun! \nYou press play and..."
  
  #display the intro
  showInformation(intro)
  
  while play == true:
    #user interaction to select puzzles, user will enter 1-4 to select from the different games
    c = requestString("Welcome to the Fabulous Betawares Puzzle Extravaganza...\n"
                      "Here is the list of puzzles: \n"
                      "  Game 1 Sound Snippetz " + solved1Display + " \n"
                      "  Game 2 Jammin' Jigsaw " + solved2Display + " \n"
                      "  Game 3 Tenacious Trivia " + solved3Display + " \n"
                      "  Game 4 Marvelous Memories " + solved4Display + " \n"
                      "Enter the number of the puzzle you wish to solve.")
    
    if c == "1":
      #call puzzle 1, needs to return a boolean value, if it returns true, the user has solved the puzzle, false indicates otherwise
      solved1 = SoundPuzzle()
      solved1Display = ' : completed'
    elif c == "2":
      #call puzzle 2
      solved2 = jigSaw()
      solved2Display = ' : completed'
    elif c == "3":
      #call puzzle 3
      solved3 = triviagame()
      solved3Display = ' : completed'
    elif c == "4":
      #call puzzle 4
      solved4 = MemoryGame()
      solved4Display = ' : completed'
    elif c == "exit":
      play == false
      break
      
    else:
      showInformation("That's an invalid input, please try again. ")
   
    #When all the games have been played, exit the loop and end the game
    if solved1 == true and solved2 == true and solved3 == true and solved4 == true:
      play = false
      win = true
  
  #outside loop
  #display the win/loss message
  if win == true:
    showInformation("Congratulations, you win. ")
  else:
    showInformation("Sorry, but you did not solve all the puzzles. ")

########
### Sound Puzzle
#for demo only:
def SoundPuzzle():
  global numBytes
  global maxAttempts
  global gameDesc
  global moveDesc
  global winMessage
  global failMessage
  global invalidEntry
  global debugFlag
  debugFlag = false
  
  currAttempt = 0
  stopGame = false
  sound = GetSound()
  
  # display the entry messages
  showInformation(gameDesc)
  
  play(sound)
  
  soundBytesDict = ChopSoundBytes(sound)
  
  # get a shuffled list - testing is done against this list
  playBytes = RandomList(numBytes)
  
  if (debugFlag):
    for i in range(0, len(playBytes)):
      printNow("i = " + str(i) + " : value = " + str(playBytes[i]))
  
  while (stopGame == false and currAttempt < maxAttempts):
    action = requestString(moveDesc)
    
    if (debugFlag and action == "original"):
      play(sound)
      continue
    
    # test for false entry
    # test for non-numeric with not 'play' or non-numerics after 'play'
    # test numerics but <0 or >6
    if ((action.isnumeric() == false 
          and action[:4].lower() != 'exit' 
          and (action[:4].lower() != 'play' or action[4:].replace(' ', '').isnumeric() == false))
       or (action.isnumeric() and (int(action) > numBytes or int(action) < 1))):
      showInformation(invalidEntry)
      continue
    
    # user selected to play a sample
    if action.isnumeric():
      if (debugFlag):
        printNow('requested index: ' + str(action) + ' : playing sample: ' + str(playBytes.index(int(action))) )
        
      # value is the number in the selected index of playBytes shuffled list
      # user selection is the value, this must be converted back to the original 1,2,3,4,5,6 index
      requestedByte = soundBytesDict[playBytes.index(int(action))]
      play(requestedByte)
    
    elif action.lower() == 'exit':
      return false
    else:
      currAttempt += 1
      # made an attempt at the game match
      resp = TestMatch(action, playBytes)
      if resp == -1:
        showInformation(tryAgainMessage)
        continue
      elif resp == 0:
        if currAttempt < maxAttempts:
          showInformation(tryAgainMessage + '\n\n'
                          'Attempt: ' + str(currAttempt) + '\n'
                          'Attempts Remaining: ' + str(maxAttempts-currAttempt))
        else:
          showInformation(failMessage)
          return false
      elif resp == 1:
        play(sound)
        showInformation(winMessage)
        return true
    #end if
  #end while
  

# test the provided string against the list of indexes and shuffled items
def TestMatch(action, playBytes):
  global debugFlag
  
  if debugFlag:
    for i in range(0, len(playBytes)):
      printNow("i = " + str(i) + " : value = " + str(playBytes[i]))
  
  searchObj = re.search(r'play ([0-9]) ([0-9]) ([0-9]) ([0-9]) ([0-9]) ([0-9])$', action, re.M|re.I)
  if searchObj:
    for i in range(0, numBytes):
      # match the value in the indexed shuffle list to the user entry
      testObj = int(searchObj.group(i+1))
      if debugFlag:
        printNow('testing index: ' + str(i))
        printNow('user entry: ' + str(testObj))
        printNow('index element 2: ' + str(playBytes.index(testObj)))
      
      if testObj < 1 or testObj > 6:
        # invalid entry
        return -1
      
      ## problem area
      if playBytes.index(testObj) == i:
        continue
      else:
        # fail!
        return 0
    #end loop - all items match
    return 1
  else:
    # searchobj not populated.  user entry is bad
    return -1
#end

# take in the full sound and chop it into smaller portions
# return the smaller portions in a dictionary
def ChopSoundBytes(sound):
  global numBytes
  global debugFlag
  soundBytesDict = dict()
  
  # loop through the soundfile and create the mini-bytes
  # each byte will be this size
  sampleBytes = getNumSamples(sound)/numBytes
  rate = getSamplingRate(sound)
  
  if (debugFlag):
    printNow("samples = " + str(getNumSamples(sound)) + " : sampleBytes = " + str(sampleBytes) + " : rate = " + str(rate))
    
  for i in range(0, numBytes):
    # range values for copying the sample values
    if i == 0:
      start = i
    else:
      start = i * sampleBytes
    
    end = start + sampleBytes
    
    if (debugFlag):
      printNow("i = " + str(i) + " : start = " + str(start) + " : end = " + str(end))

    newByte = makeEmptySound(sampleBytes, int(rate))
    
    # loop through this sample range and copy values into the new byte
    for x in range(start, end):
      #if (debugFlag):
      #  printNow("index = " + str(x-start) + " - sample = " + str(sample))
      #end if
      
      setSampleValueAt(newByte, x-start, getSampleValueAt(sound, x) * 50)
    #end loop
    
    # put the new byte in the dictionary
    soundBytesDict[i] = newByte
    
    #if (debugFlag):
    #  play(newByte)
  #end loop
  
  return soundBytesDict


# create a list of random numbers in range 1-numBytes
def RandomList(numBytes):
  items = [1, 2, 3, 4, 5, 6]    # original sound locations
  shuffle(items)                # shuffled indexes
  return items


def GetSound():
  global debugFlag
  #if debugFlag:
  #  file = pickAFile()
  #else:
  #  file = soundFilePath
  
  file = soundFilePath
  
  sound = makeSound(file)
  return sound

########

def puzzle2():
  return true

########

def puzzle3():
  return true

##############
# Memory Game

#Function to initialize the game board
def initializeGameBoard(board):
  cardNum = 0
  for i in range(boardSize):
    board.append([])
  for y in board:
    for x in range(boardSize):
      y.append(backOfCards[letters[cardNum]])
      cardNum += 1

#Function to initialize the answer board
def initializeAnswerBoard(board):
  for i in range(boardSize):
    board.append([])
  for y in board:
    for x in range(boardSize):
      index = randint(0, len(pieces)-1)
      imageNum = pieces[index]+1
      y.append(imageDict[imageNum])            
      del[pieces[index]]

#pyCopy function to copy one pictures to another            
def pyCopy(source, target, targetX, targetY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      c = getColor(getPixel(source,x,y))     #Copies the color for a pixel in the original pic
      p = getPixel(target, x+targetX, y+targetY)  #Points to the pixel of the new pic 
      setColor(p,c)
  
#Function to print out the game board           
def printBoard(board):
  for y in range(0, boardSize):
    for x in range(0, boardSize):
      pyCopy(board[y][x], tempGameBoardPic, 0+(100*x), 0+(100*y))
  repaint(tempGameBoardPic)

#Function to print the board with the tiles the user guessed as repaintn
def printBoardGuess(gBoard, aBoard, firstX, firstY, secondX, secondY):
  guessBoard = makeEmptyPicture(400, 400)
  for y in range(len(gBoard)):
    for x in range(len(gBoard)):
      if (y == firstY or y == secondY) and (x == firstX or x == secondX):
        if y == firstY and x == firstX:
          pyCopy(aBoard[firstY][firstX], guessBoard, 0+(100*firstX), 0+(100*firstY))
        elif y == secondY and x == secondX:
          pyCopy(aBoard[secondY][secondX], guessBoard, 0+(100*secondX), 0+(100*secondY))
        else:
          pyCopy(gBoard[y][x], guessBoard, 0+(100*x), 0+(100*y)) 
      else:
        pyCopy(gBoard[y][x], guessBoard, 0+(100*x), 0+(100*y))
  repaint(guessBoard)

#Function to compare two pictures to see if they are the same
def compare(pic1,pic2):
  for x in range(0,getWidth(pic1)):
    for y in range(0,getHeight(pic2)):
      if getColor(getPixel(pic1,x,y)) == getColor(getPixel(pic2,x,y)):
        continue
      else:
        return false
  return true
 
#Function to check if the guesses match each other  
def checkGuess(firstX, firstY, secondX, secondY):
  if compare(answer[firstY][firstX], answer[secondY][secondX]):
    gameBoard[firstY][firstX] = answer[firstY][firstX]
    gameBoard[secondY][secondX] = answer[secondY][secondX]
    return True
  else:
    # False - removed this line
    return False

#Function to write out the answer board to a file for testing           
def writeAnswerBoard(board):
  name = "answer.jpg"
  path = folder + name
  file = r"%s"%path
  for y in range(0, boardSize):
    for x in range(0, boardSize):
      pyCopy(board[y][x], tempGameBoardPic, 0+(100*x), 0+(100*y))
  writePictureTo(tempGameBoardPic, file)

### Memory Game main function
def MemoryGame():
  won = False
  numMatches = 0
  
  #Initialize the game, display the gameboard, and write the answer board to a file in the directory chossen. 
  initializeGameBoard(gameBoard)
  initializeAnswerBoard(answer)
  printBoard(gameBoard)
  writeAnswerBoard(answer)
  
  while not won:
    guess1Already = True
    guess2Already = True
    while guess1Already:
      guess1 = requestString("Enter the letter of the first guess, type q to quit: ").upper()
      if guess1 == 'Q':
        return False
      else:
        if compare(gameBoard[coordinates[guess1][1]][coordinates[guess1][0]], answer[coordinates[guess1][1]][coordinates[guess1][0]]):
          temp = "You already matched that square, %s. Try again"%guess1
          showInformation(temp)
        else:
          break
    while guess2Already:
      guess2 = requestString("Enter the letter of the second guess, type q to quit: ").upper()
      if guess2 == 'Q':
        return False
      else:
        if compare(gameBoard[coordinates[guess2][1]][coordinates[guess2][0]], answer[coordinates[guess2][1]][coordinates[guess2][0]]):
          temp = "You already matched that square, %s. Try again"%guess1
          showInformation(temp)
        else:
          break
    if checkGuess(coordinates[guess1][0], coordinates[guess1][1], coordinates[guess2][0], coordinates[guess2][1]):
      showInformation("Match Found!")
      numMatches += 1
      if numMatches == 8:
        showInformation("Congrats, you solved this puzzle.")
        won = True
        printBoard(gameBoard)
        return True
      printBoard(gameBoard)
    else:
      showInformation("No match, try again.")
      printBoardGuess(gameBoard, answer, coordinates[guess1][0], coordinates[guess1][1], coordinates[guess2][0], coordinates[guess2][1])
      sleep(5)
      printBoard(gameBoard)


#############
#JigSaw game
#####################################################################################################
legalMoves=['1','2','3','4','5','6','7','8','9']

def jigSaw():
  #Original Image: 5y.jpg 720x540
  #showInformation("Hello Professor,Please choose image file JigSaw_Pic.jpg or any image that is 720x540.") 
  OgPic = makePicture(getMediaPath('JigSaw_Pic.jpg'))
  
  #Blank Puzzle board/image that is the same size as the orginal
  puzzleBoard =  makeEmptyPicture(getWidth(OgPic),getHeight(OgPic))
  #Creat an empty dictionary to hold the puzzle pieces
  puzzlePieces = dict() #The set of pieces in the right order
  shufflePuzzlePieces = dict() #Shuffle the puzzle pieces
  #Switch for when the player solved the puzzle
  solved=false
   
  #Split the picture into 9 pieces
  pieceNum = 0 #To count each piece that will be created
  #Store the puzzle pieces in a dictionary
  for x in range(0,3): 
    for y in range(0,3):
      targetX = x*240
      targetY=y*180
      puzzlePieces[pieceNum] = grabPiece(OgPic,targetX,targetY)
      pieceNum = pieceNum+1
      
  #Randomize the puzzle pieces by creating a list of the dictinoary keys and shuffleing them
  shuffleKeys=[]
  for key in puzzlePieces:
   shuffleKeys.append(key)
  shuffle(shuffleKeys)
  
  #Shuffle the piece and then Piece the board together 
  order = 0
  pieceNum=0
  for x in range(0,getWidth(puzzleBoard),240):
    for y in range(0,getHeight(puzzleBoard),180):
      #Here we shuffle the pieces but still keep the dictionary keys in the order from 0 to 8  
      randomList = shuffleKeys[pieceNum] #Take an int from shuffleKeys list.
      holdRandom = puzzlePieces[randomList]  #Hold a random value(piece of the puzzle)from puzzlePieces dictionary 
      shufflePuzzlePieces[order] = holdRandom #Place that random value into the shufflePuzzlePieces dictionary
      #send to pyCopy function to put all the pieces together
      pyCopy(shufflePuzzlePieces[order],puzzleBoard,x,y)
      pieceNum = pieceNum+1
      order = order+1
      
  #show playing board for the first time
  show(puzzleBoard)
  #Display the direction and the layout of the board to the player for the first time
  jigHelp()
  
  #ASk the player for a move, test the input, and if the player made a legal move, then move the piece
  #Keep asking for a move until the player placed all the piece in the right order or unti the player asks to exit the same
  pickApiece=''
  movePieceTo=''
  while pickApiece != 'exit' or movePieceTo != 'exit': 
    #ASk the player for a move
    pickApiece = requestString("Swap piece: ").lower()
    movePieceTo = requestString("With piece: ").lower()
    if pickApiece == 'exit' or movePieceTo == 'exit':
      break
    if pickApiece == 'help' or movePieceTo == 'help':
      jigHelp() 
    if pickApiece not in legalMoves or movePieceTo not in legalMoves:
      showInformation("Im sorry, but one of those was not a legal move.") 
    if pickApiece in legalMoves and movePieceTo in legalMoves:
      #Convert user inputs to integer to use for manipulating dictonary keys
      pickedPiece = int(pickApiece)-1
      pieceToMove = int(movePieceTo)-1
      #Swap the pieces
      holdPick = shufflePuzzlePieces[pickedPiece]
      holdMoveTo = shufflePuzzlePieces[pieceToMove]
      shufflePuzzlePieces[pickedPiece]= holdMoveTo
      shufflePuzzlePieces[pieceToMove] = holdPick
      #Piece the board together with the new pieces in place
      pieceNum=0
      for x in range(0,getWidth(puzzleBoard),240):
        for y in range(0,getHeight(puzzleBoard),180):
          pyCopy(shufflePuzzlePieces[pieceNum],puzzleBoard,x,y)
          pieceNum = pieceNum+1
      repaint(puzzleBoard)
    #check to see if puzzle was solved
    if compare(OgPic,puzzleBoard) == false:
      solved = false
    if compare(OgPic,puzzleBoard)== true:
      #showInformation("Nice Job! You put all the pieces back together.")
      solved = true
      break
  #Find out if the player asked to exit the puzzle or if they solved the puzzle
  if solved == false:
    showInformation("You asked to exit this puzzle. Good Bye.")
    return false
  elif solved == true:
    showInformation("Nice Job! You put all the pieces back together.")
    return true
    
    
##################################################################################################################
# Supplemental Functions
###########################################################################################################
#This functino is passed a source image and an x and y cordinate as integers of what to copy from the source image.
#then return that piece of the image
def grabPiece(source,targetX, targetY):
  piece= makeEmptyPicture(getWidth(source)/3,getHeight(source)/3)
  for x in range(targetX, targetX+240):
    for y in range(targetY, targetY+180):
      c = getColor(getPixel(source,x,y))     #Copies the color for a pixel of source pic
      p = getPixel(piece, x-targetX, y-targetY)  #Points to the pixel in the piece pic 
      setColor(p,c)     #assigns the color of the original pic to a pixel location of the new pic
  return piece

# pyCopy function reconstructs the puzzle board 
#    source = puzzle pieces 
#    target = puzzle board
#    targetX and targetY are the x, y locations of where to copy the puzzle piece onto the puzzle board
def pyCopy(source, target, targetX, targetY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      c = getColor(getPixel(source,x,y))     #Copies the color for a pixel in the original pic
      p = getPixel(target, x+targetX, y+targetY)  #Points to the pixel of the new pic 
      setColor(p,c)     #assigns the color of the original pic to a pixel location of the new pic
  #show(target)
  return target

#This function takes two picture and compares each pixel color of both pictues
#If both pictures have the same colors for each pixel then they are the same picture and the function returns true
#Other wise if they are not the same pitcure then the function returns false
def compare(pic1,pic2):
  for x in range(0,getWidth(pic1)):
    for y in range(0,getHeight(pic2)):
      if getColor(getPixel(pic1,x,y)) == getColor(getPixel(pic2,x,y)):
        continue
      else:
        return false
  return true

#This function displays How the table is layed out, the list of legal moves and how to input a legal move
def jigHelp(): 
  showInformation("Here is how the playing board is laid out.\n [1] [4] [7] \n [2] [5] [8] \n [3] [6] [9] \nYou are only allowed to move one piece at a time.\nHere is an example of a legal move: swap block 1 with block 9.")
  showInformation("The list of legal moves are: 1, 2, 3, 4, 5, 6, 7, 8, 9, exit, help ")
  #for i in legalMoves:
    #print i
##########################################################################################################################  
def triviaquestions(x):
    questions = []  #declare question array
    answers = []  #declar answers array
    #make the trivia list
    questions.append ("What is the world's largest country?")  
    answers.append("russia")
    
    questions.append("What city has hosted more Winter Olympics than any other city in the world?")  
    answers.append("lake placid")
    
    questions.append("What is the highest level of sumo wrestling named?")
    answers.append("yokozuna") 
    
    questions.append("What is the only surviving structure of the Seven Wonders of the Ancient World")
    answers.append("pyramids")
    
    questions.append("Who is currently the most followed person on Instagram (2017)")
    answers.append("selena gomez")
    
    questions.append("What island is the home of the famed Komodo Dragon?")
    answers.append("komodo")
    
    questions.append("As of the beginning of 2018, how many movies make up the Marvel Cinematic Universe")
    answers.append("17")
    
    questions.append("What US event is held in the world's largest stadium?")
    answers.append("indianapolis 500")
    
    questions.append("When did the Tyranosaurus Rex become extinct (in years)")
    answers.append("65 million")
    
    questions.append("What Central American country boasts more colors on its flag than any other?")
    answers.append("mexico")
    
    response = requestString(questions[x])
    if response == answers[x] or response == "cheat": #can either answer question correctly or use the cheat code
        return "correct"
    else:  #anything else is wrong
        return "incorrect"
    
def triviagame():
    from random import randint
    correct = 0
    incorrect = 0
    while (correct <=3 or incorrect <=7):  # it is doing a loop until only one of the conditions is met instead of either condition met
        questnum = randint(0,9) #randomly select a question
        trivia = triviaquestions(questnum)
        if trivia == "correct":
          correct += 1 #correct counter
          showInformation("Correct!")
        elif trivia == "incorrect":
          incorrect += 1  #incorrect counter
          showInformation("Incorrect!")
        if correct == 3 or incorrect == 7:
          break
          
    if correct >=3:
        showInformation("You have won! Here is the key you seek")  #win
        return true 
    elif incorrect >=7:
        showInformation("You have failed the test.  Die Now!")  #lose
        return false
        #death 

#########
# start the game
betaGame()
