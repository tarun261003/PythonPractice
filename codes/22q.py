def water_check(x):
    water=2000
    if x>=water:
        return True
    else:
        False
test_cases=int(input('Enter no of test cases:'))
a=[]
for i in range(test_cases):
    a.append(int(input(f'Enter the test case {i+1}:')))
for i in a:
    temp="Yes" if water_check(i) else "No"
    print(temp)