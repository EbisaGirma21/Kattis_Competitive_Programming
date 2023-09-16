
n=int(input())
l={}
k=[]
y={}
for i in range(n):
    a=input()
    b=input()
    l[a] = b
m=int(input())
for i in range (m):
    k.append(input())
for key, value in l.items():
   y[value]=k.count(key)
s = dict(sorted(y.items(), key=lambda item: item[1], reverse=True))
d = list(s.items())
if(d[0][1]==d[1][1]):
    print('tie')
else:
    print(d[0][0])


