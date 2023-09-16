n,k=map(int,input().split())
l=[int(i) for i in input().split()]
f=[]
ans=[]
for i in range(1,k+1):
    f.append(l.count(i))
_min = min(f)

for i in range(len(f)):
    if f[i]==_min:
        ans.append(i+1)
print(len(ans)),
for i in ans:
    print(i,end=' ')
print()