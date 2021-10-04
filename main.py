#4x4 matrix w random static values at the beginning 
game_board = [[1024,2,4,8],[8,4,2,0],[0,0,2,0],[8,0,0,4]]
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



