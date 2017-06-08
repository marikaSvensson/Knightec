'''
def set = unordered collection with no duplicate elements. 
supports:
    - membership testing 
    - eliminating duplicate entries 
    - union
    - intersection 
    - difference
    - symmetric difference
    - etc.
'''


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print '------------------Membership:------------------'
print  'orange' in basket
print 's' in basket


a = set('abracadabra')
b = set('alacazam')
print a # unique letters in a
print b # unique letters in b
print a - b # letters in a but not in b

print a | b # letters in either a or b
print a & b # letters in both a and b
print a ^ b # letters in a or b but not both

print '---------------------list comprehensiones------------------'
c = {x for x in 'abracadabra' if x not in 'abc'}
print c













