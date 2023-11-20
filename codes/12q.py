haystack=input('Enter the string haystack:')
needle=input('Enter the string needle:')
try:
    print(haystack.index(needle))
except ValueError:
    print(-1)
