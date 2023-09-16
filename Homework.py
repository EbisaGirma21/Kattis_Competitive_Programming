n=input()

l=n.split(';')
sum=0
for i in l:
    if '-' in i:
        a,b=i.split('-')
        sum+=(int(b)-int(a)+1)
    else:
        sum+=1
print(sum)
    