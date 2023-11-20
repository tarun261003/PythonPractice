inp1=input('Enter the string :')
for i in inp1:
    if ord(i) in range(48,58) or ord(i) in range(65,91) or ord(i) in range(97,123):
        inp1=inp1.replace(i,i.lower())
    else:
        inp1=inp1.replace(i,'')
print(inp1==inp1[::-1])