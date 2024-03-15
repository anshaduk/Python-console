car={'brand':'audi','model':'q7','model':'q8'}
print(car)

bike=dict(brand='honda',model='activa')
print(bike)

#accessing value using keyname
print(car['brand'])

#accessing value using get() method
print(car.get('brand'))

#accessing keys using keys() method
car_keys=car.keys()#car_keys is a view object
print(car_keys)
car['fuel_type']='diesel'
print(car_keys)

#accessing value using values() method
car_valuse=car.values()
print(car_valuse)

#accessing items using item() method
car_item=car.items()
print(car_item)

#changing values using key names
car['model']='s5'
print(car)

#changing values using update() method
car.update({'model':'a1'})
print(car)

#adding new item using key name
car['color']='black'
print(car)

#adding new item using update() method
car.update({'capacity':'50L'})
print(car)

#removing an item using pop() method
print(car.pop('color'))#return the black
print(car)

#removing an item using popitem() method
print(car.popitem())#last item will be deleted

#removing an item using del keyword
del car['model']
print(car)

#deleting a dictinary using del
#del car
#print(car)

#emptying a dictionary using clear() method
#car.clear()
print(car)

#copying dictionary in python using copy() method
car_copy=car.copy()
print(car_copy)
car_copy['brand']='alto'
print(car_copy)
print(car)

#copying dictionary by using dict() method
bike={'model':'suzuki','type':'two wheeler'}
bike_copy=dict(bike)
bike_copy['model']='bmw'
print(bike_copy)
print(bike)


#Nested dictionaries
myfamily={
    'child1':{
        'name':'Ram',
        'age':25
    },
    'child2':{
        'name':'kumar',
        'age':30
    }
}

print(myfamily)
print(myfamily['child2']['name'])

x=('key1','key2','key3')
y=0
print(dict.fromkeys(x,y))

car={'brand':'Suzuki','model':'Sports'}
print(car)
car.setdefault('year',1991)
print(car)
