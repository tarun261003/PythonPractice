def points_assigner(n,str1):
    try:
        d={'A':'s','B':'r'}
        A,B=0,0
        for i in range(n):
            if str1[i]=='A' and d[str1[i]]=='s':
                A+=1
            elif str1[i]=='A' and d[str1[i]]=='r':
                d['A'],d['B']='s','r'
            elif str1[i]=='B' and d[str1[i]]=='s':
                B+=1
            elif str1[i]=='B' and d[str1[i]]=='r':
                d['B'],d['A']='s','r'
    except Exception as e:
        print(e)
    return [A,B]
t=int(input('Enter the number of test cases:'))
a=[]
for i in range(t):
    temp=[]
    temp.append(int(input('Enter the nunber of turns:')))
    temp.append(input('Enter the string:').upper())
    a.append(temp)
for i in a:
    s=points_assigner(i[0],i[1])
    print(s[0],end=' , ')
    print(s[1])