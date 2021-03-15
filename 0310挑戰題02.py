K=int(input("任意數:"))
n=0
l=[]

while n <= K:
    m = 11 ** n
    l.append(m)
    n += 1
for i in range(0,len(l)):
    l[i] = ' '.join(list(str(l[i])))
for i in range(0,len(l)):
    l[i] = l[i].center(len(l[-1]),' ')

sult = '\n'.join(l)
print(sult)
print("程式執行完畢!")

# inc = int(input('Input number of rows: '))
# max_len = 2 * len(str(11**inc)) - 1
# row = (' '.join([*str(11**p)]).center(max_len,' ') for p in range(inc))
# print(*row, sep='\n')