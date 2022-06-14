# os lib
import os
path = 'C:\\Users\\lovem\\Desktop\\VAkhung.txt'
if os.path.exists(path):
    print('Y')
    if os.path.isfile(path):
        print('file')
    elif os.path.isdir(path):
        print('directory')
else:
    print('no')