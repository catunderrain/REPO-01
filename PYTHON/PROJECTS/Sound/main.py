import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
from MainSub import pianonotes, randnote, songdata
import os
try:
    os.remove('main.wav')
except:
    print('none')
inputstring = 'cegabx'

inputadd = []
inputnumber = int(input())
samplerate = 4400
notefreqs = pianonotes()
musicnotes = randnote(inputnumber, inputstring, inputadd)
data = songdata(musicnotes)

data = data * (16300/np.max(data))  # đưa data cao nhất lên 16300
y = data.astype(np.int16)
print(y)
write('main.wav', samplerate, data.astype(np.int16))
print(musicnotes)

x = [i for i in range(len(y))]
plt.plot(x, y)
plt.show()
