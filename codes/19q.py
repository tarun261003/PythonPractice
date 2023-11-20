def check(inp1):
    d={'(':')','[':']','{':'}'}
    indes=[i for i in range(len(inp1))]
    even=indes[::2]
    odd=indes[1::2]
    count=0
    for i in range(len(even)):
        try:
            if d[inp1[even[i]]]!=inp1[odd[i]]:
                count+=1
        except Exception as e:
            pass
    if count==0:
        return True
    else:
        return False
inp1=input('Enter the input :')
print(check(inp1))