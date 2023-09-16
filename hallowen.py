n, m = map(str, input().split())
if(n=='NOV'):
    print('yup')
elif(n=='OCT' and int(m)==31):
    print('yup')
elif(n=='DEC' and int(m)<=24):
    print('yup')
else:
    print('nope')
    