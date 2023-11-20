n=int(input('Enter the number of rows:'))
for i in range(1,n+1):
    temp=[]
    for j in range(1,i+1):
        temp.append(str(j))
        print(j,end='')
    temp.pop()
    print(''.join(temp[::-1]))    