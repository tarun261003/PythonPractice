def adding_strings(num1,num2):
    if len(num1)<len(num2):
        num1,num2=num2,num1
    i,j,carry=len(num1)-1,len(num2)-1,0
    result=[]
    while i>=0 or j>=0 or carry:
        x=int(num1[i]) if i>=0 else 0
        y=int(num2[j]) if j>=0 else 0
        total=x+y+carry
        carry=total//10
        result.append(str(total%10))
        i-=1
        j-=1
    ans=''.join(result[::-1])
    return ans
num1=input('Enter the string 1 to add:')
num2=input('Enter the string 2 to add:')
print(f'The addition of {num1},{num2} is {adding_strings(num1,num2)}')