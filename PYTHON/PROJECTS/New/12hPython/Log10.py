#set
a = {'hello', 12, '12', 'a', 'b'}
b = {1, 12, 'b'}
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))
a.add('fuck')
a.remove(12)
c = a.union(b)
b.update(a)
print(b)
print(c)
a.clear()
print(a)