print '---------------Nested List Comprehensions -------------------'

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

m2 = [[row[i] for row in matrix] for i in range(4)]

print matrix, '\n', m2


print '------------------- transposing -------------------'

transposed = []
for i in range(4):
  transposed.append([row[i] for row in matrix])
print transposed

print '------------------- transposing2 -------------------'
transposed2 = []
for i in range(4): # the following 3 lines implement the nested listcomp
  transposed_row = []
  
  for row in matrix:
    print 'row:', row
    transposed_row.append(row[i])
    print 'transposed_row:', transposed_row
  
  transposed2.append(transposed_row)
  print 'transposed2: ', transposed2, '\n'
  
  
print transposed2

































