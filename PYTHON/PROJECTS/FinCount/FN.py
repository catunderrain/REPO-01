import numpy as np
n = int(input('Nhap gia tri n: ')) + 1
pro = []
for i in range(0, n):
    pro.append(1)
sum = 0
for i in range(0, n):
    for j in range(0, i):
        pro[i] *= j+1
    sum += pro[i]
print('F(N): ' + str(sum - 1))
