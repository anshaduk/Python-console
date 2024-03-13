#& bitwise AND
# return 1 if both of the bits are 1;else return 0
a=10
b=5
print(a&b)#in decimal
print(bin(a&b))#in binary 

#| bitwise OR
# return 1 if any one of the bit is 1;else return 0
a=10
b=5
print(a|b)#in decimal o/p=>15
print(bin(a|b))#in binary o/p =>0b1111

#~ bitwise NOT
#return one's complement of the number
#here,sighn bit is added left side ;0 for +ve number ; 1 for -ve number

a=10
print(~a)
print(bin(~a))

# ^ bitwise XOR
#return 1 if one of the bit is 1;else return 0
a=10
b=9
print(a^b)
print(bin(a^b))