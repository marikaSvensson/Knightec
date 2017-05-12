from node import Node
import time
import cProfile


L = Node("a", Node("b", Node("c", Node("d"))))
print L.value 
print L.next.value
print L.next.next.value

n = 10**4
sum = 0.0

def summation(n):
	sum = 0.0
	for i in range(n):
		sum += 1.0
	return sum
t0 = time.time()
summation(n)
t1 = time.time()
print t1 -t0


cProfile.run('summation(10000)')


