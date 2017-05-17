




a = [66.25, 333, 333, 1, 1234.5]
print  a.count(333), a.count(66.25), a.count('x')  #2 1 0

a.insert(2, -1)
a.append(333)

print a               #[66.25, 333, -1, 333, 1, 1234.5, 333]
print a.index(333)    #1

a.remove(333)
print a                #[66.25, -1, 333, 1, 1234.5, 333]

a.reverse()
print a                 #[333, 1234.5, 1, 333, -1, 66.25]

a.sort()
print a                 #[-1, 1, 66.25, 333, 333, 1234.5]


print a.pop()           #1234.5
print a                 #[-1, 1, 66.25, 333, 333]


#-----------------------------------------------------------
print "---------------------------------------------------"
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print queue  

queue.append("Terry")           # Terry arrives
print queue  


queue.append("Graham")          # Graham arrives
print queue  


print queue.popleft()                 # The first to arrive now leaves 'Eric'
print queue  

print queue.popleft()                 # The second to arrive now leaves 'John'
print queue                           # Remaining queue in order of arrival
                                  # deque(['Michael', 'Terry', 'Graham'])