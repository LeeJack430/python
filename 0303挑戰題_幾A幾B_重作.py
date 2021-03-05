def _rdA():
    Ans=[]
    while True:
        sS=random.randint(1,9)
        if sS not in Ans:
            Ans.append(sS)
        if len(Ans) == 4:
            break
    return(Ans)
    
import random 

anS=_rdA()
cou=1

while True:
    aA=0
    bB=0
    Key=input("請輸入4個1~9不重複的數字(按Q離開):")
        
    if Key.upper()=="Q":
        print("程式結束!")
        break
    
    if Key.isnumeric():
        Gu=list(Key)
        if len(Gu) != 4 :
            print("輸入錯誤！請重新輸入")
            continue
    
        for n in range(4):
            if anS[n] == int(Gu[n]):
                aA += 1
            elif int(Gu[n]) in anS:
                bB += 1
        print("{0}.{1}A.{2}B".format(cou,aA,bB))
        
        if aA == 4 :
            print("猜對了!總共猜了{}次".format(cou))
            YN = input("要再玩一次嗎?(Y/N)")
            if YN.upper() == "Y":
                cou=1
                anS=_rdA()
                continue
            else:
                print("程式結束!")
                break
        cou += 1
    else:
        print("輸入錯誤！請重新輸入")
        continue
   