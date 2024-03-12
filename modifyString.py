#uppercase
txt="hello world"
print(txt.upper())

#lowercase
txt="HELLO WORLD"
print(txt.lower())

#remove white space
txt=" hello world "
print(txt.strip())

#replace string
txt="hello world"
print(txt.replace('hello','j'))

#split 
txt="hello world"
print(txt.split(","))

#string format 
age=10
txt='my name is john, and i m {}'
print(txt.format(age))

quantity=3;
price=300;
itemno=2;
txt='i want to pay {1} dollar for {2} pieces of item {0}.'
print(txt.format(quantity,price,itemno))

#escape character
txt="Hello this is \"Anshad\" from india";
print(txt)