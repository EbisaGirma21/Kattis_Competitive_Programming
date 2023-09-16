n = input()
l = n.split(' ')
is_repeated = False

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            is_repeated = True
            break  
if is_repeated:
    print('no')
else:
    print('yes')
