import collections
def unique(lst):
    temp=[]
    d=collections.Counter(lst)
    a=list(d.keys())
    b=[int(i) for i in a]
    k=len(b)
    temp.append(k)
    temp.append(sorted(b))
    return temp
lst=list(map(int,input('Enter the list with spaces:').split()))
answer=unique(lst)
print(answer[0],end=',')
dashes=['-']*(len(lst)-len(answer[1]))
answer[1].extend(dashes)
print(answer[1])