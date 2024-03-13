#single dimensional list
numbers=[1,2,3,4,"abc",3.24]
print(type(numbers))
print(numbers[4])

#multi dimensional list
items=[[1,2,3],"hello",[4,5,6]]
print(items[0][0])
print(items[1])
print(items[2][1])


newList=[[1,2,3],[['a','b','c'],5,6]]
print(newList[1][0][1])
# a=newList[1]
# b=a[0]
# print(b[1])
print(newList[1][1])

#Adding element to list
# 1.append() to add item at the end of the list
languages=['c','cpp','java']
languages.append('python')
print(languages)

#2.insert() to add an item at a specific position
languages=['c','cpp','java']
languages.insert(0,'python')
print(languages)

#3.extend() to add all items of one list in another list
languages=['c','cpp','java']
more_languages=['.net','python']
languages.extend(more_languages);
print(languages)

#input a list using loop
n=int(input("Enter the limit:"))
number=[]
for i in range(n):
    x=int(input())
    number.append(x)
print(number)

#range
for i in range(0,3):
    print('Hello,Dear..!')

#input a list using split method
n=int(input('enter the number of element:'))
numbers=input(f'Enter the {n} numbers:').split()
for i in range(0,n):
    numbers[i]=int(numbers[i])
print(numbers)

#changing an item of list
myList=['sam','ram',1,2,3,4.567]
myList[1]='amna'
print(myList)

#changing multiple item in a list using SLICING
myList[2:4]=['a','b','c']
print(myList)

#insert a new item in list
myList=[1,2,3,4]
myList.insert(2,1000)
print(myList)

#Remove an item from the list using remove() method
list=[1,2,3,4]
list.remove(2)
print(list)

#Remove an item using POP(index) method
list.pop(1)#to remove 1st index item
print(list)

list=[1,2,3,4,5]
print(list.pop())