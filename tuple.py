cars=('Auadi','BMW','Alto','Alto')
print(cars)
print(cars[0])#accessing tuple item through positive index
print(cars[-1])#accessing tuple item through negative index;Last item of tuple
print(cars[1:3])#accessing tuple item through slicing
print(len(cars))#length of tuple


cars=tuple(('Alto','bmw','benz'))
print(cars)

#Adding an item into tuple
#tuple is immutable ; 1st convert tuple into list by using list() method
bike=('Honda','Suzuki','Activa')
temp=list(bike)#convert tuple into list
temp.append('bmw')
bike=tuple(temp)#convert list into tuple
print(bike)

#update tuple
bike=('Honda','Suzuki','Activa')
temp=list(bike)
temp[1]='bmw'
bike=tuple(temp)
print(bike)

#unpacking a tuple
bike=('Honda','Suzuki','Activa')
bike1,bike2,bike3=bike
print(bike3)

#use asterik(*)
cars=('audi','mercedes','bmw','toyota','ferari')
car1,*car2,car3=cars
print(car1)
print(car2)
print(car3)

#loop through the tuple
cars=('audi','mercedes','bmw','toyota','ferari')
for i in cars:
    print(i)

for i in range(len(cars)):
    print(cars[i])

tuple1=(1,2,3)
tuple2=('a','b','c')
tuple3=tuple1+tuple2
print(tuple3)

t1=(1,2,3,2)
print(t1.count(2))
print(t1.index(2))
print(t1*2)