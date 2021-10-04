# #4x4 matrix w random static values at the beginning 
# game_board = [[4,8,8,0],[4,4,2,0],[0,0,2,0],[8,0,0,4]]

import random
import copy

sizeOfBoard = 4

def printLikeMatrix():
#finding out largest elemnt on board and then deciding number of spaces to make the board consistent
  largestElemOnBoard = game_board[0][0]
  for row in game_board:
    for num in row:
      if num>largestElemOnBoard:
        largestElemOnBoard = num
  
  spacesNeeded = len(str(largestElemOnBoard))



  for row in game_board:
    currentRow = "|"
    #if list has a 0 , it needs to print space
    for num in row: 
      if num == 0:
        currentRow+= " "*spacesNeeded + "|"
      else:
        currentRow+=(" "*(spacesNeeded-len(str(num)))) + str(num)+"|"
    print(currentRow)
  print()



# printLikeMatrix()

#function to merge the current row towards the left
def mergeL(row):
  for j in range(sizeOfBoard-1):
    for i in range(sizeOfBoard-1,0,-1):
  #check if the before space is empty & if it is push/move everything to left
      if row[i-1] == 0:
        row[i-1]= row[i]
        row[i] = 0

  #merging happens now
  for i in range(sizeOfBoard-1):
    #check if next value and the current value are same
    if row[i] == row[i+1]:
      #if it is same then multiply the current value by 2 and assign the next value as 0
      row[i]*=2
      row[i+1] = 0 

  
  for i in range(sizeOfBoard-1,0,-1):
#shift everything towards left again
    if row[i-1] == 0:
      row[i-1]= row[i]
      row[i] = 0
  return row

#function to merge the entire board towards left in 1 go
def mergeLeftFully(curBoard):
  for i in range(sizeOfBoard-1):
    curBoard[i] = mergeL(curBoard[i])
  
  return curBoard


def reverseRow(row):
  #add all numbers from the current row to a new list to reverse it
  newList = []
  for i in range(sizeOfBoard-1,-1,-1):
    newList.append(row[i])
  return newList





#function to merge the entire board towards left in 1 go
def mergeRightFully(curBoard):
  for i in range(sizeOfBoard):

  #to merge right -> reverse current row merge to left and reverse again to merge right
    curBoard[i] = reverseRow(curBoard[i])
    curBoard[i] = mergeL(curBoard[i])
    curBoard[i] = reverseRow(curBoard[i])
  return curBoard  
  


def transposeRow(curBoard):
  for j in range(sizeOfBoard):
    for i in range(j,sizeOfBoard):
      if not i == j:
        temp = curBoard[j][i]
        curBoard[j][i] = curBoard[i][j]
        curBoard[i][j] = temp
  return curBoard  
#function to merge board upwards
def mergeUpFully(curBoard):
  #transpose board merge left and then transpose again to merge up
  curBoard = transposeRow(curBoard)
  curBoard = mergeLeftFully(curBoard)
  curBoard = transposeRow(curBoard)

  return curBoard

#function to merge board downwards
def mergeDownFully(curBoard):
  #transpose board merge oight and then transpose again to merge down
  curBoard = transposeRow(curBoard)
  curBoard = mergeRightFully(curBoard)
  curBoard = transposeRow(curBoard)

  return curBoard




#adds a 2 or a 4 to the board at the beginning using random fucntion
def addRandValue():
  if random.randint(1,8) == 1:
    return 4
  else:
    return 2


#adding a new value after every move to a random space
def addRandNewValue():
  rowNum = random.randint(0,sizeOfBoard-1) 
  colNum = random.randint(0,sizeOfBoard-1) 
  #find empty spot 
  while not game_board[rowNum][colNum] == 0:
        rowNum = random.randint(0,sizeOfBoard-1) 
        colNum = random.randint(0,sizeOfBoard-1) 
  
  #populate this empty spot w a value
  game_board[rowNum][colNum] = addRandValue() 


#empty board -> fill matrix w 0's first and then adding 2 numbers to the main matrix -> can be 2 or 4
game_board = []
for i in range(sizeOfBoard):
  row = []
  for j in range(sizeOfBoard):
      row.append(0)
  game_board.append(row)   

#minimum 2 values needed to start game
minNum = 2
while minNum > 0:
  #choosing random row and column
  rowNum = random.randint(0,sizeOfBoard-1) 
  colNum = random.randint(0,sizeOfBoard-1) 

  #if spot picked = empty add a randum value from function above and reduce minNum
  if game_board[rowNum][colNum] == 0:
    game_board[rowNum][colNum] = addRandValue()
    minNum-=1

printLikeMatrix()


isGameOver = False

while not isGameOver:
  inp = input("move which way? ")

  valInp = True

  tempGameBoard = copy.deepcopy(game_board)

  if inp == "d":
    game_board = mergeRightFully(game_board)
  
  
  elif inp == "a":
    game_board = mergeLeftFully(game_board)

  
  elif inp == "w":
    game_board = mergeUpFully(game_board)

  
  elif inp == "s":
    game_board = mergeDownFully(game_board)
  
  else:
    valInp = False
  

  if not valInp:
    print("Enter a valid input")
  else:
    if(game_board == tempGameBoard):
      print("move unsuccessful try another direction")
    else:
      addRandNewValue()
      printLikeMatrix()
