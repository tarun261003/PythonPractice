def no_of_years(x,y,z):
    return (y-x)//z
test_cases=int(input('Enter no of test cases:'))
a=[]
for i in range(test_cases):
    a.append(list(map(int,input(f'Enter the test case {i+1}:').split())))
for i in a:
    print(no_of_years(i[0],i[1],i[2]))