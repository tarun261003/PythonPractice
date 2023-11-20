inp1=input('Enter a string :')
subs=[inp1[i:j] for i in range(len(inp1)) for j in range(i+1,len(inp1))]
palindrome=[i for i in subs if i==i[::-1]]
palindrome.sort(key=len)
print("The Largest sub string in the",inp1,"is :",palindrome[-1])