def smallest_N(n,k):
    if n<k:
        return n
    else:
        while n>=0:
            temp=n
            n-=k
        return temp
test_cases=int(input('Enter no of test cases:'))
a=[]
for i in range(test_cases):
    a.append(list(map(int,input(f'Enter the test case {i+1}:').split())))
for i in a:
    print(smallest_N(i[0],i[1]))