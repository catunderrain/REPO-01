# exception
try:

    a = int(input('a: '))
    b = int(input('b: '))
    c = a/b
    print(c)
except Exception as e:
    print(e)
else:
    print('Okay')
finally:
    print('Damn')

        