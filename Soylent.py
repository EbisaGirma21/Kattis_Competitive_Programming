import math


n=int(input())
for i in range(n):
    l=int(input())
    if(l%400==0):
        print((l//400))
    else:
        print(math.ceil(l/400))