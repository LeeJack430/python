def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

Key=int(input('輸入任意數:'))
ans=[]

for i in range(2,Key+1):
    if Key % i == 0 and is_prime(i):
        ans.append(i)

print("{}的質因數為:{}".format(Key,ans))
print('-'*50)
print('%d='%Key,end='')
while Key>1:
    for j in range(2,Key+1):
        if Key%j==0:
            Key=int(Key/j)
            if Key==1:
                print('%d'%j,end='')
            else:
                print('%d*'%j,end='')
                break
print()