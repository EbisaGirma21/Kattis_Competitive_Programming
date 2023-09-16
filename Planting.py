m=input()
n= input()
l = list(map(int, n.split()))
l.sort(reverse=True)
f=[]
for index,num in enumerate(l):
    f.append(index+num+1)
print(max(f)+1)
