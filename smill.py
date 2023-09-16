n = input()
l = [':)', ';)', ':-)', ';-)']
for i in range(0,len(n)+1):
    for j in range(i,len(n)+1):
        if(n[i:j] in l):
            print(i)