#4x4 matrix w random static values at the beginning 
game_board = [[0,2,4,8],[8,4,2,0],[0,0,2,0],[8,0,0,4]]
def printLikeMatrix():
  for row in game_board:
    currentRow = "|"
    #if list has a 0 , it needs to print space
    for num in row: 
      if num == 0:
        currentRow+= " |"
      else:
        currentRow+=str(num)+"|"
    print(currentRow)
  print()

printLikeMatrix()



