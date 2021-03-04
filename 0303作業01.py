import random as rd
count=0
ans = rd.randint(1,100)
guess = 0
Max=100
Min=0
while ans != guess:
    guess = int(input("請輸入1~100之間的整數:"))
    if ans>guess:
        Min=guess
        print("{}~{},猜大一點".format(Min,Max))
    if ans<guess:
        Max=guess
        print("{}~{},猜小一點".format(Min,Max))
    count +=1
print("正解!總共猜了",count,"次")
print("程式結束")