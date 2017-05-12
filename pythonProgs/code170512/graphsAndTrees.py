

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



