def dishes_check(n,x,y,z):
    N=0
    if y>1:
        N=min(x,y)
        y=abs(N-y)
        N+=min(y,z)
    elif y==1:
        N=1
    else:
        N=0
    if N>=n:
        return True
    else:
        return False
test_cases=int(input('Enter no of test cases:'))
a=[]
for i in range(test_cases):
    a.append(list(map(int,input(f'Enter the test case {i+1}:').split())))
try:
    for i in a:
        temp="Yes" if dishes_check(i[0],i[1],i[2],i[1]) else "No"
        print(temp)  
except Exception as e:
    print("Something Went Wrong!!")