def hexrand():
    import random
    return '#{:06x}'.format(random.randint(0, 0xffffff))


print(hexrand())
