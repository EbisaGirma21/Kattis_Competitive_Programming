l=[]

while True:
    n=input()
    if(n=='***'):
        break
    l.append(n)
s=set(l)
theSame=''
original=''
cnt=0
for i in s:
    d=l.count(i)
    if(d>cnt):
        cnt=d
        original=i
        theSame=''
    elif(d==cnt):
        theSame=i
        break

if(theSame!=''):
    print('Runoff!')
else:
    print(original)

    