#dictionary
alpha = {1: 'a',
         2: 'b',
         3: 'c',
         4: 'd'}
print(alpha[1])
print(alpha.get('c'))
print(alpha.keys())
print(alpha.values())
print(alpha.items())
for a, b in alpha.items():
    print(a, b)
alpha.update({5: 'e'})
alpha.update({1: 'z'})
print(alpha)
print(alpha.pop(2))
print(alpha.clear())