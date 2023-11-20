roman=input("Enter the roman value to get the Numerical value:").upper()
r_d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
two_len=[roman[i:i+2] for i in range(len(roman)-1)]
two_len1=[i for i in two_len if i in r_d.keys()]
if(two_len1!=[]):
    for i in two_len1:
        roman=roman.replace(i,'')
    sum=0
    for i in roman:
        sum+=r_d[i]
    for i in two_len1:
        sum+=r_d[i]
else:
    sum=0
    for i in roman:
        sum+=r_d[i]
print(sum)
