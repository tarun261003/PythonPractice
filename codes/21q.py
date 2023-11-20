n=int(input('Enter the number of elements you want to enter:'))
a=[]
for i in range(n):
    a.append(int(input(f'Enter {i+1} element:')))
a.sort()
print(a)