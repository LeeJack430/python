from math import sqrt

def f(num):
    for x in range(0,num):
        m=sqrt(x+100)
        n=sqrt(x+168)
        if m == int(m) and n==int(n):
            print(x)

print(f(1000))