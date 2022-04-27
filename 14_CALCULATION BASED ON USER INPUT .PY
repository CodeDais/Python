a=int(input('enter first value'))
b=int(input('enter second value'))

ch=input('Enter a chiose \n add \n sub \n mul \n div \n')

if ch=='add':
    print(a+b)
elif ch=='sub':
    print(a-b)
elif ch=='mul':
    print(a*b)
elif ch=='div':
    print('a/b')
else:
    print('Invalid Option')
