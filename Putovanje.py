n,m=map(int,input().split())
l=[int(i) for i in input().split()]
ans=0
for i in range(len(l)):
    max=0
    count=0
    for j in range(i,len(l)):
        if(max+l[j]<=m):
            max+=l[j]
            count+=1
    if(count>=ans):
        ans=count
print(ans)
            