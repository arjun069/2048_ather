#4x4 matrix w random static values at the beginning 
game_board = [[1024,2,4,8],[8,4,2,0],[0,0,2,0],[8,0,0,4]]


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

printLikeMatrix()


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
