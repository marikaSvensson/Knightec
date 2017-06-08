knights = {'gallahad': 'the pure', 
           'robin': 'the brave'}

for (keys, values) in knights.items():
  print '(keys, values): ', (keys, values)
  

print knights['gallahad']

'''
When looping through a sequence, the position index and corresponding value can be retrieved at the same time using
the enumerate() function.
'''
for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)


'''To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
'''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
  print('What is your {0}? It is {1}.'.format(q, a))
  
  
  
  