def sum(x,y):
    s=6
    if x+y>s:
        return True
    else:
        False
test_cases=int(input('Enter no of test cases:'))
a=[]
for i in range(test_cases):
    a.append(list(map(int,input(f'Enter the test case {i+1}:').split())))
for i in a:
    temp="Yes" if sum(i[0],i[1]) else "No"
    print(temp)