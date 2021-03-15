Key=int(input("輸入年利潤:"))
pf={'10W':0.1,'20W':0.075,'30W':0.03,'10Wb':10000,'20Wb':7500}

pfk =list(pf.keys())
pfv =list(pf.values())

if Key <= 100000 :
    print('年利潤{}以下'.format(pfk[0]))
    print('獎金為:',Key*pfv[0])
    print('程式執行完畢')
    
if Key < 200000 and Key > 100000  :
    print('年利潤{}~{}'.format(pfk[0],pfk[1]))
    c=Key-100000
    b=c*pfv[1]
    print('獎金為:',b+pfv[3])
    print('程式執行完畢')

if Key < 300000 and Key > 200000  :
    print('年利潤{}~{}'.format(pfk[1],pfk[2]))
    c=Key-200000
    b=c*pfv[2]
    print('獎金為:',b+pfv[3]+pfv[4])
    print('程式執行完畢')
    
if Key >= 300000:    
    print('年利潤{}'.format(Key))
    c=Key-300000
    b=c*pfv[2]
    print('獎金為:',b+pfv[3]*2+pfv[4])
    print('程式執行完畢')