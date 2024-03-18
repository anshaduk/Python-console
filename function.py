#function definition
# def calc_sum(num1,num2):
#     return num1+num2

# res=calc_sum(10,6)
# print(res)

# res=calc_sum(10,20)
# print(res)
# str1='hello'
# str2='world'

cities=['kozhikode','nadakkavu','kakkodi','chelannur']
language=['english','malayalam','hindhi','urudu','tamil']
def cal_length(list):
    print(len(list))

# cal_length(cities)
# cal_length(language)
    
#print list in single line
def print_list(list):
    for item in list:
        print(item,end=" ")

# print_list(cities)

#factorial of number
n=5

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
#calc_fact(5)
    
#convert USD into INR
def convert(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")

# convert(2)
    
#Odd or Even
def oddEven(num):
    if(num%2==0):
        print(num,"is Even")
    else:
        print(num,"is Odd")
#oddEven(5)
        
#recursion
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
#show(5)

#sum of n numbers
def sumOfN(n):
    if n==0:
        return 0 
    return sumOfN(n-1)+n
res=sumOfN(5)
#print(res)

#list print
def print_list(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=['mango','banana','apple','grape']
#print_list(fruits)

#Arbitary argumets *args
def my_func(*kids):
    print('The youngest child is '+kids[0])

#my_func('sam','ram','kumar','vasu')

#keyword arguments kwargs
def my_func(child3,child2,child1):
    print('The youngest child is '+child2)

#my_func(child1='sam',child2='raju',child3='siva')

#Arbitary keyword arguments **kwargs
def my_func(**kid):
    print('His last name is '+kid['lname'])
#my_func(fname='siva',lname='kumar')

#default parameter
def my_func(country="india"):
    print('my country is '+country)
# my_func('japan')
# my_func('pakisthan')
# my_func()
    
#passing list as an argument
def my_func(food):
    for i in food:
        print(i)

fruits=['mango','apple','banana']
# my_func(fruits)

#pass statement
def my_func():
    pass
#my_func()

#position only argument
def my_func(x,/):
    print(x)
#my_func(3)

#keyword only argument
def my_func(*,x):
    print(x)
#my_func(x=3)

#combined position only and keyword only arguments
def my_func(a,b,/,*,c,d):
    print(a+b+c+d)
#my_func(2,3,c=4,d=5)

#lambda function
add=lambda a,b:a+b
#print(add(5,10))

#lambda using multiplay 2 numbers 
#IIFE
#print((lambda a,b:a*b)(3,4))

#use default Prameter
add=lambda x,y=15,z=20:x+y+z
#print(add(10))

#use arbitary argument
addition=lambda *args:sum(args)
#print(addition(20,40,60))

#high-order function
high_order_function=lambda x,fun:x+fun(x)
#print(high_order_function(20,lambda x:x*x))

#even or odd
#print((lambda x:(x%2 and 'odd' or 'even'))(3))
#print((lambda x:'even' if x%2==0 else 'odd')(30))

#substring check
sub_string=lambda str:str in 'welcome to bridgeon'
print(sub_string('java'))

