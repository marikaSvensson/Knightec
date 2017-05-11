filename = 'input.txt'
infile = open(filename,r) # open and read
line = infile.readlin() # read line 1
# read coordinates, store in regular arrays!
x = [] 
y = []

for line in infile:
  words = line.split() # split the line into words
  x.append(float ( words[0] )
  #y.append(float ( words[1] )
  
infile.close()