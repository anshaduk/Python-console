from functools import reduce

#filter
nums=[2,4,3,5,7,8,6,10]
even=list(filter(lambda n:n%2==0,nums))
print(even)

#map
double=list(map(lambda n:n*2,even))
print(double)

#reduce
sum=reduce(lambda a,b:a+b,double)
print(sum)