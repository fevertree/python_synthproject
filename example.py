# original code from http://codingmess.blogspot.com.ee/2008/07/how-to-make-simple-wav-file-with-python.html

import numpy as N
import wave
import matplotlib.pyplot as plt
from basic_units import radians, degrees, cos
import pyaudio

p = pyaudio.PyAudio()

class SoundFile:
   def  __init__(self, signal, duration, samplerate):
		self.frequency = frequency
		self.duration = duration
		self.file = wave.open('test.wav', 'wb')
		self.signal = signal
		self.sr = samplerate

   def write(self):
       self.file.setparams((1, 2, self.sr, self.sr*self.duration, 'NONE', 'noncompressed'))
       self.file.writeframes(self.signal)
       self.file.close()

# let's prepare a signal
volume =  16384
A = 1
duration = 2 # seconds
#number of samples of audio carried per second. 44.1 kHz is the sampling rate of audio CDs
#20 kHz is the highest frequency audible by humans
samplerate = 44100 # Hz
#amount of samples needed to fill n seconds of audio
samples = duration*samplerate
#number of    phases (cycles) per second
frequency = 261.63 # Hz

# sine wave has a phaseic form which repeats every T seconds
phase = samplerate / float(frequency) # in sample points

omega = N.pi * 2 / phase
# omega = 1-(1/N.pi*phase)

#creates an array of evenly spaced intervals and multiplies each value with the omega
period = N.arange(int(phase),dtype = N.float) * omega

#sin wave
y = A * N.sin(period)
#sawtooth wave
# y = A - ((A / N.pi) * period)

ydata = volume * y

#length of signal is the size of the samples (duration*samplerate)
#N.resize makes a new array called signal which has the length of the samples
#The command then fills it with repeated copies of the ydata
signal = N.resize(ydata, (samples,))

stream = p.open(format=8,
                channels=1,
                rate=samplerate,
                output=True)

ssignal = ''
for i in range(len(signal)):
   ssignal += wave.struct.pack('h',signal[i]) # transform to binary

# f = SoundFile(ssignal,duration,samplerate)
# f.write()


x = [val*radians for val in period]
fig = plt.figure()
ax = fig.add_subplot(211)
line1 = ax.plot(x, y, xunits=radians)
plt.show()


stream.write(ssignal)

stream.stop_stream()
stream.close()

p.terminate()

