fruits=['grapes','apple','banana','mango']
fruits_len=len(fruits)
index=0
while index<fruits_len:
    if fruits[index] == 'orange':
        print('Orange is available')
        break
    index+=1
else:
    print("Orange is not available")
