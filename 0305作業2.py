import  random

Ans=[]
while True:
    sS=random.randint(1,49)
    if sS not in Ans:
        Ans.append(sS)
    if len(Ans) == 6:
        break
print("隨機選號為:",Ans)

