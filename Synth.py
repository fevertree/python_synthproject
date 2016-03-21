import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Music

class Synth():

	def __init__(self,tempo):
		self.volume = 16384
		self.samplerate = 44100
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format=8,channels=1,rate=self.samplerate,output=True)
		self.totalsignal = []
		self.m = Music.Music()
		self.tempo = tempo
		self.BPS = 60 / tempo

	def __enter__(self):
		return self

	def playSignal(self, signal):
		self.stream.write(signal)

	def genNote(self,note,beats,type):
		duration = self.BPS * beats
		frequency = self.m.returnFreq(note)
		A = 1
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
		
		return ssignal

	def genChord(self,notes,duration,type):
		notedata = []
		for note in notes:
			signal = self.genNote(note,duration*2,type)
			decodeddata = np.fromstring(signal, np.int16)
			notedata.append(decodeddata * 0.5)
			
		return sum(notedata).astype(np.int16)

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


