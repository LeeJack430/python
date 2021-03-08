number=list()
while len(number) <= 4 :
    num=int(input("請輸入數字:"))
    number.append(num)
print("串列內容:",number)
temp= number.copy()
cou=0
for i in range(len(temp)):
    cou += 1
    n=len(temp)
    for j in range(len(temp)):
        if temp[j]>temp[i]:
            temp[j],temp[i] = temp[i],temp[j]
    print("這是第{}次排序,排序完的資料{}".format(cou,temp))

print("氣泡排序法結果:",temp)