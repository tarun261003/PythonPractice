def repeatedSub(str1):
    length=len(str1)
    for i in range(1,length//2+1):
        if length%i==0:
            substr=str1[:i]
            if substr * (length//i) == str1:
                return True
    return False
str1=input('Enter the string to check the substring repeatition:')
print(repeatedSub(str1))