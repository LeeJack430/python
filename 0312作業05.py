import copy
lisT1=[1,3,5,7,9]
lisT2=[]

lisT2= copy.copy(lisT1)
print("串列lisT1=",lisT1)
print("串列lisT2=",lisT2)
print('-'*50)
lisT2.append(11)
print("串列lisT1=",lisT1)
print("串列lisT2=",lisT2)