import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Synth():

	def __init__(self):
		self.volume = 16384
		self.samplerate = 44100
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format=8,channels=1,rate=self.samplerate,output=True)
		self.notes = {"C":261.63, "D":293.66, "E":329.63, "F":349.23, "G":392.0,"A":440.0, "B":493.88}
		self.totalsignal = []

	def __enter__(self):
		return self

	def playSignal(self, signal):
		self.stream.write(signal)

	def genNote(self,note,duration,type):
		A = 1
		frequency = self.notes[note]
		samples = duration*self.samplerate
		phase = self.samplerate / float(frequency)
		omega = np.pi * 2 / phase
		period = np.arange(int(phase),dtype = np.float) * omega

		if type == "sin":
			y = A * np.sin(period)
		if type == "saw":
			y = A - ((A / np.pi) * period)

		ydata = self.volume * y
		signal = np.resize(ydata, (samples,))

		ssignal = ''
		for i in range(len(signal)):
		   self.totalsignal.append(signal[i] / self.volume)
		   ssignal += wave.struct.pack('h',signal[i])
		
		# self.playSignal(ssignal)
		return ssignal
	

	def visualize(self):

		def animate(i):
			l = len(self.totalsignal)
			x = np.arange(int(l))
			y = [s for s in self.totalsignal]
			y = y[:len(x)]
			xs = []
			ys = []
			for n in range(l):
				xs.append(x[n])
				ys.append(y[n])
			ax.clear()
			ax.plot(xs, ys)

		# l = len(self.totalsignal)
		# xLen = l
		# x = np.arange(int(xLen))
		# y = [s for s in self.totalsignal]
		# y = y[:len(x)]
		fig = plt.figure()
		ax = fig.add_subplot(211)
		# line1 = ax.plot(x, y)
		ani = animation.FuncAnimation(fig, animate, interval=1000)
		plt.show()



	def __exit__(self, exc_type, exc_value, traceback):
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()


