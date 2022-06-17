import numpy as np
import os
import wave
import struct
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


# xoa file cu
try:
    os.remove('ds.wav')
except:
    print('none')
# tinh so mau cua frame
file = wave.open('abc.wav', 'r')
length = file.getnframes()
print(length)
# lay mau du lieu
ray = []
for i in range(0, length):
    wavedata = file.readframes(1)
    data = struct.unpack("<h", wavedata)
    datas = -int(data[0])
    ray.append(int(round(datas, 0)))
ray = np.array(ray)
print(ray)
# viet file tai tao
write('ds.wav', 4400, ray.astype(np.int16))
# ve do thi song am
y = ray.astype(np.int16)
x = np.array([i for i in range(length)])
plt.plot(x, y)
plt.show()
