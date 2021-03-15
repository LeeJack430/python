a,b=2,1
c=0
l=[]
for i in range(20):
    c += a/b    
    a = a+b
    b = a-b
    l.append(c)
print(c)
print(l)