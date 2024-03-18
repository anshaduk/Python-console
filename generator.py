#defining a generator
# def gen1():
#     yield 10
#     yield 20
#     yield 30

# x=gen1()
# for i in x:
#     print(i)


# print(next(x))
# print(next(x))
# print(next(x))

# def gen2():
#     for i in range(11):
#         yield i
# y=gen2()
# for i in y:
#     print(i)

#Iterator
fruits=('orange','mango','apple','grapes')
itr_ob=iter(fruits)
print(next(itr_ob))
print(next(itr_ob))
print(next(itr_ob))
# raise StopIteration()
print(next(itr_ob))