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
print(res)

#list print
def print_list(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=['mango','banana','apple','grape']
print_list(fruits)