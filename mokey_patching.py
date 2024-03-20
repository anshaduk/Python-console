import Test_monkey

def cube(self,num):
    return f"cube of the number is {num**3}"

#monkey patching
Test_monkey.power.square=cube
obj=Test_monkey.power()
print(obj.square(3))