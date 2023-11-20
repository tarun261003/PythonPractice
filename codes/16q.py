def anagram(st1,st2):
    lst1=list(st1)
    lst2=list(st2)
    lst1.sort()
    lst2.sort()
    if lst1==lst2:
        return True
    else:
        return False
st1=input('Enter the string 1:').lower()
st2=input('Enter the string 2:').lower()
print(anagram(st1,st2))