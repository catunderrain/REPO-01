# Hex Random
def randhex():
    import random
    def r(): return random.randint(0, 255)
    return '#{:02x}{:02x}{:02x}'.format(r(), r(), r())


print(randhex())
