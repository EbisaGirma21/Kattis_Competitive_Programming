n=int(input())
prev=1
isOdd=False
isEven=False
sum=0
for i in range(1,100):
    for j in range(i,i+n):
        sum+=j
    if sum%2==0:
        isEven=True
    else:
        isOdd=True
    sum=0
if(isEven and isOdd):
    print('Either')
elif(isEven):
    print('Even')
else:
    print('Odd')
        