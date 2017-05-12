

print hash(42)

name1 = "Marika"
name2 = "Anders"
print hash(name1+name2)

print "-------- Adjacent lists--------"

a, b, c, d, e, f, g, h = range(8)
N = [
{b, c, d, e, f}, # a
{c, e}, # b
{d}, # c
{e}, # d
{f}, # e
{c, g, h}, # f
{f, h}, # g
{f, g} # h
]

for i in range(8):
  print "N[%d]: " %(i)
  print N[i]

print "N[v] <=>  reperesents the set of v's neighbours"
print (b in N[a]) # Neighborhood membership
print len(N[f]) # Degree

M = [
[b, c, d, e, f], # a
[c, e], # b
[d], # c
[e], # d
[f], # e
[c, g, h], # f
[f, h], # g
[f, g] # h
]

for i in range(8):
  print "M[%d]: " %(i)
  print M[i]


#dicts instead of sets or lists. 
# neighbours = keys
# can accosiate neighbour to wieght ( int)
O = [
{b:2, c:1, d:3, e:9, f:4}, # a
{c:4, e:3}, # b
{d:8}, # c
{e:7}, # d
{f:5}, # e
{c:2, g:2, h:2}, # f
{f:1, h:6}, # g
{f:9, g:8} # h
]

for i in range(8):
  print "O[%d]: " %(i)
  print O[i]

print b in O[a] # Neighborhood membership
print len(O[f]) # Degree
print O[a][b] # Edge weight for (a, b)

print "Arbitrary, hashable. node lable --> dict is main structure"
P = {
'a': set('bcdef'),
'b': set('ce'),
'c': set('d'),
'd': set('e'),
'e': set('f'),
'f': set('cgh'),
'g': set('fh'),
'h': set('fg')
}

#for i in range(8):
#  print "P[%d]: " %(i)
print len(P)
print 'a' in P
print P['a']

print ("--------------------- Adjency Matrices -------------------------")

# a b c d e f g h
NN = [
[0,1,1,1,1,1,0,0], # a
[0,0,1,0,1,0,0,0], # b
[0,0,0,1,0,0,0,0], # c
[0,0,0,0,1,0,0,0], # d
[0,0,0,0,0,1,0,0], # e
[0,0,1,0,0,0,1,1], # f
[0,0,0,0,0,1,0,1], # g


[0,0,0,0,0,1,1,0]
] # h

print NN[a][b] # Neighborhood membership
print sum(NN[f]) # Degree





































