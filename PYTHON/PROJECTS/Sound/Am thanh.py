import numpy as np
import os
import wave
import struct
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import random

# detect file vao
filein = 'brown.wav'

# xoa file cu
try:
    os.remove('soundrecovery.wav')
except:
    print('none')

# tinh so mau cua frame
file = wave.open(filein, 'r')
length = file.getnframes()
print(length)

# lay mau du lieu
sound_array = []
for i in range(0, length):
    wavedata = file.readframes(1)
    data = struct.unpack("<h", wavedata)
    datas = int(data[0])
    sound_array.append(int(round(datas, 0)))
sound_array = np.array(sound_array)
print(sound_array)
print(max(sound_array), min(sound_array))

# viet file tai tao
write('soundrecovery.wav', 4400, sound_array.astype(np.int16))

# ve do thi song am
y = sound_array.astype(np.int16)
x = np.array([i for i in range(length)])
plt.plot(x, y)
plt.show()
