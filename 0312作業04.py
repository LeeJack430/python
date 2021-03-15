lisT=[]
cou=3
while len(lisT) <=2 :
    Key=int(input("請輸入3個數，還剩下{}個數:".format(cou)))
    lisT.append(Key)
    cou -= 1
    continue  
print(sorted(lisT))    
print('程式執行完畢')