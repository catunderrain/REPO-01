import shutil
import os
a = 'a.txt'
b = 'b.txt'
#os.replace(a, b) # del a, move data a to b
try:
    os.rmdir('del')
    os.remove('b.txt')
    
except Exception:
    print('')

shutil.rmtree('del')
