def frequency(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
n=int(input('Enter the number of strings you need to enter:'))
a=[]
for i in range(n):
    a.append(input(f'Enter the string {i+1}:'))
subs=[]
for i in a:
    temp=[]
    for j in range(1,len(i)+1):
        subs.append(i[0:j])
common=[]
d=frequency(subs)
for i in d:
    if d[i]>1:
        common.append(i)
if common==[]:
    print("")
else:
    print(common[-1])