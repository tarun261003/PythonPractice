def happy_checker(inp1):
    vowels=list('aeiou')
    count=0
    subs=[inp1[i:j] for i in range(len(inp1)) for j in range(i+1,len(inp1))]
    subs.sort(key=len)
    substrings=[i for i in subs if len(i)>2]
    for str1 in substrings:
        count=0
        for i in str1:
            if i in vowels:
                count+=1
        if len(str1)==count:
            return True
    return False
t=int(input('Enter no of test cases:'))
a=[]
for i in range(t):
    a.append(input(f'Enter the string {i+1}:'))
for i in a:
    temp="Yes" if happy_checker(i) else "No"
    print(temp)