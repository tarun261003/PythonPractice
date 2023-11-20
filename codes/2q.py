print("Enter the elements of the list:")
lst=list(map(int,input().split()))
key=int(input('Enter the key element:'))
count=0
for i in range(len(lst)):
    if count!=0:
        break
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==key:
            print([i,j])
            count+=1
            break
if(count==0):
    print("There is no combination:(")