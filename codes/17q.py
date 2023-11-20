def frequency(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
nums=list(map(int,input('Enter the num elements:').split()))
d=frequency(nums)
a=list(d.keys())
a.sort(reverse=True)
try:
    print(a[2])
except Exception as e:
    print(a[0])