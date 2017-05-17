# find a celebrity (knows none everybody knows the celcbrity)
from functions import *
from random import randrange
n = 5
G = [[randrange(2) for i in range(n)] for i in range(n)]

c = randrange(n)
for i in range(n):
  G[i][c] = True
  G[c][i] = False
print G

print  celeb(G)
print G
print "True = ", True
print "False = ", False

if (1): print "true is 1"
if (0): print "true is 0"