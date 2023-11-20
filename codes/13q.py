lst=list(map(int,input('Enter the list elements by space:').split()))
n=int(input('Enter the key element:'))
count=0
for i in range(len(lst)):
    if lst[i]==n:
        count+=1
        print(i)
if count==0:
    print('Element Not found')