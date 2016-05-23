import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Music
import Signal

class Synth():

	def __init__(self,tempo):
		self.volume = 16384
		self.samplerate = 44100
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format=8,channels=1,rate=self.samplerate,output=True)
		self.totalsignal = []
		self.m = Music.Music()
		self.tempo = tempo
		self.BPS = 60.0 / tempo
		# self.signalLog = open("signalLog.txt", 'r+')
		self.frameCounter = 0

	def __enter__(self):
		return self

	def playSignal(self, signal):
		for s in signal.signalData:
			self.totalsignal.append(s)
		self.stream.write(signal.binary)

	def genNote(self,note,beats,type):
		signalObject = Signal.Signal()

		duration = self.BPS * beats
		if len(note) > 0:
			frequency = self.m.returnFreq(note)
			phase = self.samplerate / float(frequency)
			omega = np.pi * 2 / phase
		else:
			frequency = 0
			phase = 0
			omega = 0
		A = 1

		samples = duration*self.samplerate
		period = np.arange(int(phase),dtype = np.float) * omega

		if type == "sin":
			y = A * np.sin(period)
		elif type == "saw":
			y = A - ((A / np.pi) * period)

		ydata = self.volume * y
		signal = np.resize(ydata, (samples,))

		ssignal = ''

		for i in range(len(signal)):
		   	signalObject.signalData.append(signal[i] / self.volume)
		   	signalObject.binary += wave.struct.pack('h',signal[i])
		
		return signalObject

	def genChord(self,notes,duration,type):
		signalObject = Signal.Signal()
		notedata = []
		signalDatas = []

		for note in notes:
			signal = self.genNote(note,duration*2,type)
			signalDatas.append(signal.signalData)
			decodeddata = np.fromstring(signal.binary, np.int16)
			notedata.append(decodeddata * 0.5)

		signalObject.signalData = sum(map(np.array, signalDatas))
		signalObject.binary = sum(notedata).astype(np.int16)

		return signalObject

	def visualize(self):

		fig, ax = plt.subplots()
		ax.set_ylim(-6, 6)

		ydata = []
		for i in range(len(self.totalsignal)):
			ydata.append(self.totalsignal[i])
		# xdata = np.arange(len(ydata))

		x = np.arange(1000)
		line, = ax.plot(x, ydata[0:1000])

		def animate(i):
			if 1000*i+1000 > len(ydata):
				pass
			else:
				line.set_ydata(ydata[1000*i:1000*i+1000])
  				return line,
		def init():
			line.set_ydata(np.ma.array(x, mask=True))
	 		return line,

	 	frames = len(ydata) /1000

		ani = animation.FuncAnimation(fig, animate,frames, init_func=init,
		                              interval=100, blit=True,repeat = True)
		plt.show()


	def playSong(self, song):

		generatedNotes = {}

		for note in song:
			noteList = note.split(' ')
			if noteList[0] == 'pause':
				if note not in generatedNotes:
					generatedNotes[note] = self.genNote("",float(noteList[-1]),"saw")
			elif len(noteList) == 2:
				if note not in generatedNotes:
					generatedNotes[note] = self.genNote(noteList[0],float(noteList[-1]),"saw")
			else:
				if note not in generatedNotes:
					generatedNotes[note] = self.genChord(noteList[:len(noteList)-1],float(noteList[-1]),"saw")

		for note in song:
			self.playSignal(generatedNotes[note])

	def __exit__(self, exc_type, exc_value, traceback):
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()
		# self.signalLog.close()


