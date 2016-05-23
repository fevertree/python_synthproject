from Synth import Synth
import numpy as np
from Music import Music
import Signal
import thread

#sepapoisid

m = Music()

superMario = [
			 "E F#/Gb4 D 0.25",
			 "E F#/Gb4 D 0.25",
			 "pause 0.25",
			 "E F#/Gb4 D 0.25",
			 "pause 0.25",
			 "C F#/Gb4 D 0.25",
			 "E F#/Gb4 D 0.25",
			 "pause 0.25",
			 "G B G5 0.25",
			 "pause 0.75",
			 "G G G 0.25",
			 "pause 0.75",
			 "C E G 0.25",
			 "pause 0.5",
			 "G C E 0.25",
			 "pause 0.5",
			 "E G C 0.25",
			 "pause 0.5",
			 "A C F 0.25",
			 "pause 0.25",
			 "B D G 0.25",
			 "pause 0.25"
			 "A#/Bb C#/Db F#/Gb 0.25",
			 "A C F 0.25",
			 "pause 0.25",
			 "G C E 0.30",
			 "E G C 0.30",
			 "G B E 0.30",
			 "A C F 0.25",
			 "pause 0.25",
			 "F A D 0.25",
			 "G B E 0.25",
			 "pause 0.25",
			 "E A C 0.25",
			 "pause 0.25",
			 "C E A 0.25",
			 "D F B 0.25",
			 "B D G 0.25",
			 "pause 0.5",
			 "C E G 0.25",
			 "pause 0.5",
			 "G C E 0.25",
			 "pause 0.5",
			 "E G C 0.25",
			 "pause 0.5",
			 "A C F 0.25",
			 "pause 0.25",
			 "B D G 0.25",
			 "pause 0.25",
			 "A#/Bb C#/Db F#/Gb 0.25",
			 "A C F 0.25",
			 "pause 0.25",
			 "G C E 0.30",
			 "E G C 0.30",
			 "G B E 0.30",
			 "A C F 0.25",
			 "pause 0.25",
			 "F A D 0.25",
			 "G B E 0.25",
			 "pause 0.25",
			 "E A C 0.25",
			 "pause 0.25",
			 "C E A 0.25",
			 "D F B 0.25",
			 "B D G 0.25",
			 "pause 0.5",
			 "C 0.25",
			 "pause 0.25",
			 "G E 0.25",
			 "F#/Gb D#/Eb G 0.25",
			 "F D 0.25",
			 "D#/Eb B 0.25",
			 "C 0.25",
			 "E C 0.25",
			 "pause 0.25",
			 "G#/Ab E 0.25",
			 "A F 0.25",
			 "C G C 0.25",
			 "C 0.25",
			 "A C 0.25",
			 "C E F 0.25",
			 "D F 0.25",
			 "C 0.25",
			 "pause 0.25",
			 "G E 0.25",
			 "F#/Gb D#/Eb E 0.25",
			 "F D 0.25",
			 "D#/Eb B 0.25",
			 "G 0.25",
			 "E C C 0.25",
			 "pause 0.25",
			 "A G F5 0.25",
			 "pause 0.25",
			 "A G F5 0.25",
			 "A G F5 0.25",
			 "pause 0.5",
			 "G 0.25"
			 ]

Cmaj = m.returnMajorScale("C",4)
print Cmaj

with Synth(100.0) as syn1:

	syn1.playSong(superMario)

	# C = syn1.genNote("C",0.5,"sin")
	# E = syn1.genNote("E",0.5,"sin")
	# G = syn1.genNote("G",0.5,"sin")
	# cMaj = syn1.genChord(["C","E","G"],0.5,"sin")
	# pause = syn1.genNote("",0.1,"sin")

	# syn1.playSignal(C)
	# syn1.playSignal(pause)
	# syn1.playSignal(E)
	# syn1.playSignal(pause)
	# syn1.playSignal(G)
	# syn1.playSignal(pause)
	# syn1.playSignal(cMaj)

	# syn1.visualize()

	