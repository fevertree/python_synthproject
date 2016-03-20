import numpy as np
import wave
import pyaudio

class Synth():

	def __init__(self):
		self.volume = 16384
		self.samplerate = 44100
		self.buffer = ''
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format=8,channels=1,rate=self.samplerate,output=True)
		self.notes = {"C":261.63, "D":293.66, "E":329.63, "F":349.23, "G":392.0,"A":440.0, "B":493.88}

	def playSignal(self, signal):
		self.stream.write(signal)

	def genNote(self,note,duration,w):
		A = 1
		frequency = self.notes[note]
		samples = duration*self.samplerate
		phase = self.samplerate / float(frequency)
		omega = np.pi * 2 / phase
		period = np.arange(int(phase),dtype = np.float) * omega

		if w == "sin":
			y = A * np.sin(period)
		if w == "saw":
			y = A - ((A / np.pi) * period)

		ydata = self.volume * y
		signal = np.resize(ydata, (samples,))

		ssignal = ''
		for i in range(len(signal)):
		   ssignal += wave.struct.pack('h',signal[i])

		self.playSignal(ssignal)

	def close(self):
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()



