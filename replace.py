# str="I love mangoes, Do you love..?"
# print(str.replace('love','hate'))
# print(str.replace(' ','-',3))

l = [1, 2]
# r=''.join(map(str,l))
r=''.join(str(i) for i in l)
print(r)

a1=" hello"
print(a1.isalpha())
