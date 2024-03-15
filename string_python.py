#backslash is used escape the character
# print("Hello ! \"Good morning\" how\'s the situation")

#multi-line ''' OR """
# statement=""""Hello !
# This is Anshad,
# How are you..."""
# print(statement)

# str="Hello"
# print(str[0])
# print(str[-1])
# print(str[1:4])

#string concantination + 
# x="I"
# y=" am"
# z=" Anshad"
# print(x+y+z)

#String Repetetion operator *
# print(3*'Anshad')
# print('Anshad'*3)
# print(0*'Anshad')
# print(-3*'Anshad')

#string comparison operator
#== return true if two string are equal
# print('Hello'=='Hello')#True
# print('Hello'=='hello')#False

#!= operator
#Return true if two strings are not equal
# print('Hello'!='hello')#True

#< operator
#return true 1st string is smaller than 2nd string
# str1="Hello"
# str2="welcome"
# print(str1<str2)#True

# #>
# print('hello'>='Hello')

#string formatting operator %
age=25
print('My age is ',age)

#slicing with third parameter
str="I am Jaspreet"
print(str[2:10:2])

#string interpolation
#adding external object into a string
#%s placeholder
name="Anshad"
age=25
print("Hello ,this is %s and age is %d" %(name,age))

#str.format() function
#{} place holder
name="sam"
place="delhi"
print("my name is {} and i m from {}".format(name,place))

#f string
x=10
y=20
print(f"The sum of {x+y} is {x+y}" )