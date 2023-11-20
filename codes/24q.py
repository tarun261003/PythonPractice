def no_of_pages(x,y):
    return x*y
test_cases=int(input('Enter no of test cases:'))
a=[]
for i in range(test_cases):
    a.append(list(map(int,input(f'Enter the test case {i+1}:').split())))
for i in a:
    print(no_of_pages(i[0],i[1]))