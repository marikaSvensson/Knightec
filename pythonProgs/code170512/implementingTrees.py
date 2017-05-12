T = [["a", "b"], 
["c"], 
["d", 
["e", "f"]]
]
print T[0][1]

print T[2][1][0]


from tree import BinaryTree
from tree import MultiwayTree

t = BinaryTree(BinaryTree("a", "b"), BinaryTree("c", "d"))
print t.right.left
print t

tM = MultiwayTree(MultiwayTree("a", MultiwayTree("b", MultiwayTree("c", MultiwayTree("d")))))
print tM.kids.next.next.val

from tree import Bunch
x = Bunch(name="Jayne Cobb", position="Public Relations")
print x.name

T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))
print t.left
print  t.left.right
print t['left']['right']
print "left" in t.right
print "right" in t.right

from random import randrange
L = [randrange(10000) for i in range(1000)]
print 42 in L
S = set(L)
print 42 in S
