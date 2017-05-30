a = [66.25, 333, 333, 1, 1234.5]
print "a:               ", a
print "count:            ", a.count(333), a.count(66.25), a.count('x')

a.insert(2, -1)
a.append(333)
print "insert, append:    ", a

print "a.index(333):      ", a.index(333)

a.remove(333)
print "a.remove(333), a:  ", a

a.reverse()
print "a.reverse(), a:     ", a

a.sort()
print "a.sort(),a:          ", a

print "a.pop():              ", a.pop()
print "a:                    ", a
