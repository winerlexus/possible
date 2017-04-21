from itertools import *
##count=0
##for i1 in range(0,10):
##        for i2 in range(0,10):
##            for i3 in range(0,10):
##                for i4 in range(0,10):
##                     numb=i1,i2,i3,i4
##                     for tp in range(0,len(numb)-1):
##                         if numb[tp]==numb[tp+1]:
##                             count+=1
##print(count)
                            
a=list(product(range(3),repeat=4))
##print(a[0:20])
aplist=[]
for i in range(0,len(a)):
    for i1 in range(0,3):
        if a[i][i1]==a[i][i1+1]:
            aplist.append(a[i])     
clear=(set(aplist))
print(clear)
print(len(clear))
