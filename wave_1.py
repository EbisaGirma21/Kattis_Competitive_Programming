n=input()
prev=''
count=0
l=0
for i in n:
    if(prev!=i):
        count+=1
        prev=i
    else:
        prev=i
        count=1
    l=max(count,l)
print(l)