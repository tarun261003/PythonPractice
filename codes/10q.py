from nine import *
a=[]
n=int(input('Enter the index needed:'))
for i in range(n+1):
    temp=[]
    for j in range(i+1):
        temp.append(combinations(i,j))
    a.append(temp)
print(a[n])