def fact(i):
    if i==0 or i==1:
        return 1
    else:
        return i*fact(i-1)
def combinations(n,r):
    return fact(n)//(fact(r)*fact(n-r))
if __name__=="__main__":
    a=[]
    n=int(input('Enter the number of rows required:'))
    for i in range(n):
        temp=[]
        for j in range(i+1):
            temp.append(combinations(i,j))
        a.append(temp)
    print(a)