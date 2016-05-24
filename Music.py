import math

class Music():

	def __init__(self):
		self.a = float(math.pow(2.0,1.0/12.0))
		self.f0 = 16.35 # C0
		self.noteNames = ['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']
		octaves = 8

	def returnFreq(self, note):
		"""Returns the frequency for a specified note in a specified octave. Defaults to the
		4th octave if not specified."""

		def hasOctave(inputString):
			"""Checks if the inputted note has an octave specified"""
			return any(char.isdigit() for char in inputString)

		if hasOctave(note):
			octave = int(note[-1])
			pos = self.noteNames.index(note[0:len(note)-1])
		else:
			octave = 4
			pos = self.noteNames.index(note)

		notes = len(self.noteNames)
		
		halfTones = octave * notes + pos

		return self.f0 * math.pow(self.a,halfTones)

	def returnMajorScale(self,parallelKey,octave):
		"""Returns a list of notes for a specified major scale and octave"""
		oc = octave
		notes = []
		notes.append("%s%s" % (parallelKey, str(oc))) 
		structure = [1,1,0.5,1,1,1,0.5]
		pos = self.noteNames.index(parallelKey)
		
		for n in structure:
			pos += n*2
			if pos > len(self.noteNames)-1:
				pos -= 12
				oc += 1
			notes.append("%s%s" % (self.noteNames[int(pos)],str(oc)))				

		return notes