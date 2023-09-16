n = [1, 1, 2]
s = set(n)
l = list(s)
for i in range(len(n) - len(s)):
    l.append('_')
f = ', '.join(str(i) if i == '_' else str(i) for i in l)
print(f'{len(s)}, nums = [{f}]')
