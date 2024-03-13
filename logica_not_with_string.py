#the strring is empty NOT operator return True
name='john'
if not name:#name is  empty
    print('no name')
else:
    print(f'your name is {name}')

#list dictionary tuple is empty NOT operator return True
names=['Ram','Sam','Kuamr']
if not names:
    print('no names')
else:
    print(f'There are total of {len(names)} names')