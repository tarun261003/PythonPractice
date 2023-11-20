def avg(a):
    sum=0
    for i in a:
        sum+=float(i)
    return sum/len(a)
t=int(input('Enter the no of test cases:'))
names=[]
marks=[]
d={}
for i in range(t):
    inp1=input('Enter the record with spaces:').split()
    d[inp1[0].lower()]=[inp1[1],inp1[2],inp1[3]]
query=input('Enter the student name:').lower()
print("%.2f"%(avg(d[query])))