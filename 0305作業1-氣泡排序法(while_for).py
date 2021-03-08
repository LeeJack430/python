number=list()
while len(number) <= 5 :
    num=int(input("請輸入數字:"))
    number.append(num)
print("串列內容:",number)
temp= number.copy()
cou=0
while True:
    cou += 1
    n=len(temp)
    for i in range(n-1):
        if temp[i]>temp[i+1]:
            temp[i],temp[i+1] = temp[i+1],temp[i]
    print("這是第{}次排序,排序完的資料{}".format(cou,temp))
    if temp[n-1]>temp[n-2]>temp[n-3]>temp[n-4]>temp[n-5]:
        break
print("氣泡排序法:",temp)