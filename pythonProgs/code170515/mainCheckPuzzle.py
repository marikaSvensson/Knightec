from CheckPuzzle import cover
from CheckPuzzle import trav

row = 8
col = 8

board = [[0]*col for i in range(row)] # Eight by eight checkerboard
board[row-1][col-1] = -1 # Missing corner


#for r in range(row):
#  for c in range(col):  
#      board[r][c] = r+c
  

print cover(board)

for r in board:
  print((" %2i"*col) % tuple(r))


print trav(range(100))