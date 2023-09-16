n,m=map(int,input().split())
l=[]
for i in range(m):
    x,y=map(int,input().split())
    l.append((x,y))
l.sort(key=lambda x: x[1])
t=-1
c=0
for i,j in l:
    if t<=i:
        t=j
        c+=1
if(c>=n):
    print('YES')
else:
    print('NO')