print "#------------------ List Comprehensions -----------------------"
squares1 = squares2 =  squares3 = []
for x in range(10):
  squares1.append(x**2)
print squares1

squares2 = list(map(lambda x: x**2, range(10)))
print squares2

squares3 = [x**2 for x in range(10)]
print squares3

print "# --------------------------------------------------"
vec = [[1,2,3], [4,5,6], [7,8,9]]
a = [num for elem in vec for num in elem]
a2 = [num for elem in vec ]

print "for loop:"
for elem in vec: 
  for num  in elem: 
    print elem, num


print num
print elem
print vec
print a
print a2

print "#------------------------- tuple ---------------------------------------"
t1  = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print t1


combs = []
for x in [1,2,3]:
  for y in [3,1,4]:
    if x != y:
      combs.append( (x,y) )
print combs

print "---------------------- lists of strings ----------------------------------"
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
freshfruit2 = [weapon.strip() for weapon in freshfruit]

print freshfruit, '\n',freshfruit2

print "------------------- math and rounding ------------------------------------"
from math import pi
piList = [str(round(pi, i)) for i in range(1, 6)]
print piList




