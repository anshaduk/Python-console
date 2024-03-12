#capitalize first letter to uppercase
txt="hello"
print(txt.capitalize())

#casefold,lower string into lowercase
txt="HELLO"
print(txt.casefold())

#center returned a centered string
txt='hello is world'
print(txt.center(30))

#count return no of time specified value occured in a string
txt="apple is ,an apple ,apple is red color"
print(txt.count('a'))

#encode return the encoded version of the string
txt='hello world'
print(txt.encode())

#endswith return true a string ends with a specified value
txt="hello,this is Bridgeon"
print(txt.endswith("."))

#expandtabs sets tab size of the string
txt="h\te\tl\tl\to"
print(txt.expandtabs(2))

#find position where it was found
txt='hello ,welcome to my world'
print(txt.find('w'))

#join joints the elements of an iteratable to the end of string
txt=('john','mark','alice')
print('#'.join(txt))

#maketrans return a translation table to be used in translation
txt="Hello sam"
mytable=txt.maketrans('s','p');
print(txt.translate(mytable))

#partition where the string is parted into 3
txt="i could eat banana all day"
print(txt.partition('eat'))

#swapcase upper to lower and vice versa
txt="Hello worlD ,MY"
print(txt.swapcase())

#title to convert first letter of each word into uppercase
txt="welcome to my world"
print(txt.title())

#translate returned a translate string
txt="hello Sam"
mydict={83:80}
print(txt.translate(mydict))

#zfill add 0 at the begning of the string with reaches the specified length
txt='hello';
print(txt.zfill(10))