from turtle import color
import matplotlib.pyplot as plt
import numpy as np
#
div = 0.01
rans = -10
rane = 10

num = int((rane - rans)/div)
#
x = [round(div*k + rans, 2) for k in range(0, num+1)]
y = [(4*np.sinc(10*t)) for t in x]
print(np.pi)
#
a = 0
#
plt.plot(x, y)
y = [0 for t in x]
plt.plot(x, y, color='red')
b = x
a = [0 for t in b]
plt.plot(a, b, color='red')
plt.show()
