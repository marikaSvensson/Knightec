
print "--------------------------- new dict md ---------------------"
md = {'a':1, 'b': 2 }
kk = md.keys()
print "kk[0]:       ", kk[0]
print "kk[:]:       ", kk[:]
print "md[kk[0]]:   ", md[kk[0]]
print "1 in md:     ", 1 in md
print "kk[0] in md: ", kk[0] in md
print "kk[1] in md: ", kk[1] in md
print "md.get:      ", md.get( 'a' )
print "items:       ", md.items()
print "len:         ", len(md)
print "iter(md):    ", iter(md)
print "md.copy():    ", md.copy()
print "pop:          ", md, md.pop(kk[0]), md
md['c'] = 3
print md
#print md, "md.popitem:", md.popitem(), md.popitem(), md  
print md.setdefault('d'), md, md.keys()
md.update(red=1, blue=2)
print md
print "values():      ", md.values()
print 1 in md.values()
print 9 in md.values()
#print "--------------------------- new dict c ---------------------"
#c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#print c