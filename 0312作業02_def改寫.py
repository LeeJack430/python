def bonus(money):
    tn=0.1
    tw=0.075
    th=0.03
    tnb=100000*0.1
    twb=100000*0.075
    if money <= 100000 :
       bo=money*tn 
    
    if money < 200000 and Key > 100000  :
       bo=money-100000
       bo=bo*tw
       bo=bo+tnb
    
    if money < 300000 and Key >= 200000  :
       bo=money-200000
       bo=bo*th
       bo=bo+tnb+twb
        
    if money >= 300000: 
       bo=money-300000
       bo=bo*th
       bo=bo+tnb+tnb+twb
       
    return bo
        
Key=int(input("輸入年利潤:"))
print('年利潤為:{}獎金為:{}'.format(Key,bonus(Key)))
print('程式執行完畢')