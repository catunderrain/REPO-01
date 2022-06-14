# str.format
a = 'what'
b = 'the'
c = 'fuck'
num = 3.14159265
num2 = 1234
print('{:<10} {} {} {d}!'.format(a, b, c, d = 'bro'))
print('{:>10} {} {} {d}!'.format(a, b, c, d = 'bro'))
print('{:^10} {} {} {d:^20}!'.format(a, b, c, d = 'bro'))
print('A {:^10.2f} B'.format(num))
print('{:x}'.format(num2))