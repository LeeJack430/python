# n=int(input("任意數:"))
n=4

for i in range(n+1):
    print(" "*(n-i)+"*"*(2*i-1))

for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
    
print("程式執行完畢")