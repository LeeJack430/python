number=int(input("請輸入次數:"))
lisT1=[]
#lisT2=[]

for i in range(1,number+1):
     if i %2 == 0 :
         lisT1.append(i)

# for I in range(1,number+1):
#     if I %2 == 1 :
#         lisT2.append(I)

print(lisT1,"皆為偶數")
# print(lisT2,"皆為奇數")
print(sum(lisT1),"為偶數總和")
print("程式結束")