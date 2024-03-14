set1={1,True,2.4,-5,0,2,4,3,2}
print(set1)

#create an empty set
set2={1}
print(type(set2))

#Add an item into set using add() method
set1={1,2,4,'sam',3.5,False,0}
set1.add(100)
print(len(set1))

#remove() method used to remove an item
set1.remove(1)
print(set1)

#discard() method used to remove an item
set1.discard(4)
print(set1)

#clear() method used to delete all item OR emptying the set
set1.clear()
print(set1)

#pop() method is used to remove a random item from the set
set2={2,4,6,7,3,"abc"}
print(set2.pop())
print(set2)

set2.add((2,4,67,89))#add tuple into an set ;but list is not allowed in set Bcz list is mutable.
print(set2)

#Operation on set
#union 
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3={'ram','raju'}
print(set1.union(set2,set3,[100,200,1]))
#print(set1|set2|set3)#union of set1 and set2

#intersection
#print(set1.intersection(set2))
print(set1&set2)

#upadte sets using update() method
set1.update(('@','$'))
print(set1)

#intersection_update
set1.intersection_update(set2)
print(set1)

set2.intersection_update(['shyam','kumar'])
print(set2)

#difference
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3={'ram','raju'}
set1.difference(set2)
print(set1)
#OR
set1-set2
print(set1)

#diff_update
set1.difference_update(set2)
print(set1)

#symmetric_diff
set1.symmetric_difference(set2)
print(set1)

#symmetric_diff_update
set1.symmetric_difference_update(set2)
print(set1)

set2.symmetric_difference_update(set1)
print(set2)

#isdisjoint()
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.isdisjoint(set2))#False bcz duplicate value here

#issubset;<=
print(set1.issubset(set2))

#issuperset;>=
print(set1.issuperset(set2))
