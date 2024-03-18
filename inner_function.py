def area(l,b,r):
    def circle(r):
        return 3.14*r*r
    def rectangle(l,b):
        return l*b
    return circle(r)+rectangle(l,b)

res=area(10,10,10)
print(res)