import numpy as np
n = [6,7,1,1,5,6,8]
n.sort(reverse = True)
print(n)
cost = 20
sumc = 0
read = []
write = []
t = True
print(n[0])
while t == True:
    
    for i in n:
        sumc = sumc + i
        if cost > sumc:
            read.append(i)
            pass
        else:
            n.remove(i)
    write.append(read)
    sumc = 0
    read = []
    if n != []:
        n.remove(n[0])
        t = True
    else:
        t = False
print(write)