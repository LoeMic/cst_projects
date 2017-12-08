#JigSaw Puzzle
#Piece of the Final Project
#By:Patrick Gonzalez
#######################################################################################################################
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
 ####################################################################################################################### 
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
######################################################################################################################
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
################################################################################
#This function displays How the table is layed out, the list of legal moves and how to input a legal move
def help(): 
  showInformation("Here is how the playing board is laid out.\n [1] [4] [7] \n [2] [5] [8] \n [3] [6] [9] \nYou are only allowed to move one piece at a time.\nHere is an example of a legal move: swap block 1 with block 9.")
  showInformation("The list of legal moves are: 1, 2, 3, 4, 5, 6, 7, 8, 9, exit, help ")
  #for i in legalMoves:
    #print i
##########################################################################################################################  

#Main Puzzle function  
import random
legalMoves=['1','2','3','4','5','6','7','8','9',]
exitNhelp =['exit','help']

def jigSaw():
  #Original Image: 5y.jpg 720x540
  printNow("Please choose image file 5y.jpg")
  OgPic = makePicture(pickAFile())  
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
  random.shuffle(shuffleKeys)
  
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
  for i in shufflePuzzlePieces:
    print i
  #Display the direction and the layout of the board to the player
  help()
  
   
  #ASk the player for a move, test the input, and if the player made a legal move, then move the piece
  #Keep asking for a move until the player placed all the piece in the right order or unti the player asks to exit the same
  pickApiece=''
  movePieceTo=''
  while pickApiece != 'exit' or movePieceTo != 'exit': 
  #while solved == false: 
    pickApiece = requestString("beging flag:Swap piece: ").lower()
    movePieceTo = requestString("begin flag:With piece: ").lower()
    if pickApiece == 'exit' or movePieceTo == 'exit':
      break
    if pickApiece == 'help' or movePieceTo == 'help':
      help() 
    if pickApiece not in legalMoves or movePieceTo not in legalMoves:
      showInformation("Im sorry, but one of those was not a legal move.") 
    if pickApiece in legalMoves and movePieceTo in legalMoves:
      #Convert user inputs to ints to use for the manipulating dictonary keys
      pickedPiece = int(pickApiece)-1
      pieceToMove = int(movePieceTo)-1
      #Swap the pieces
      holdPick = shufflePuzzlePieces[pickedPiece]
      holdMoveTo = shufflePuzzlePieces[pieceToMove]
      shufflePuzzlePieces[pickedPiece]= holdMoveTo
      shufflePuzzlePieces[pieceToMove] = holdPick
      #Piece the board together with the new piece in place
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
      #showInformation("Nice Job! You put all the piece backtogether.")
      solved = true
      break
  #Find out if the player asked to exit the puzzle or if they solved the puzzle
  if solved == false:
    showInformation("You asked to exit this puzzle. Good Bye.")
    exit
  elif solved == true:
    showInformation("Nice Job! You put all the piece backtogether.")
    exit
  
  
 
  
  
  
  
  
  
  
