def make_word():
    word = ''
    for w in 'spam':
        word += w
        yield word
        
        
        
list1 = list(make_word())
print(list1)

list_gener = (x for x in range(10))
next(list_gener)
print('teste1', next(list_gener))
# >> 0

for i in list_gener:
  print('teste2 ',i)