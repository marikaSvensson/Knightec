# Huffman's algorithm:

#----------------------
from heapq import heapify, heappush, heappop
from itertools import count
#-------------

def huffman(seq, frq):
  num = count()
  trees = list ( zip( frq, num, seq ))    # num ensures valid ordering
  heapify(trees)                          # A min-heap based on frq
  
  
  while len(trees) > 1:                    # Until all are combined
    fa, _, a = heappop(trees)              # Get the two smallest trees
    fb, _, b = heappop(trees)
    n = next(num)
    
    heappush(trees,   (fa+fb, n, [a,b])  )      # Combine and re-add them
  
  return trees[0][-1]