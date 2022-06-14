# *args = *[name] : tuple

def add(*args):
    print(args)
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4))
