
print    '------------------------------- Tuples -------------------------------'
t = 12345, 54321, 'hello!'
print t

u = t, (1, 2, 3, 4, 5)
print u

print   '\n -----Tuples are immutable but they can contain mutable objects:----'
v = ([1, 2, 3], [3, 2, 1])
print v

print   '\n -------Demonstrating mutable objects inside immutable tuples:------'
print (v[0])[1] 
(v[0])[1] = 1000
print (v[0])[1]
print v 