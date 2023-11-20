def frequency(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
a=list(map(int,input('Enter the array elements with spaces:').split()))
d=frequency(a)
for i in d:
    if d[i]==1:
        print(f'The single number is {i}')
