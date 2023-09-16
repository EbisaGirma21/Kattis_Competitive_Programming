l=[int(i) for i in input().split()]
b=(l[1]-l[0])*l[2]
a=0
cnt=0
while a<=b:
    a+=l[-1]
    cnt+=1
print(l[3]+cnt)