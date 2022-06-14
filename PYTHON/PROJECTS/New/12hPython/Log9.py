#tuple
a = ('hello', 21, 'kay')
print(a.count(21))
print(a.index('kay'))
print([a[i] for i in range(len(a))])
if 21 in a:
    print('yes')