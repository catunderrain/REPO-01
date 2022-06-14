file = open('python/projects/files/data.txt', 'a')
fil = open('python/projects/files/data.txt', 'r')
file.write('hello')

print(fil.read())
file.close()
