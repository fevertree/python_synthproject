from Synth import Synth
import numpy as np
from Music import Music
import Signal

#sepapoisid

m = Music()

Cmaj = m.returnMajorScale("C",4)

with Synth(100.0) as syn1:
	# syn1.visualize()

	# C = syn1.genNote("C",0.25,"saw")
	# E = syn1.genNote("E",0.25,"saw")
	# G = syn1.genNote("G",0.25,"saw")
	# cMaj = syn1.genChord(["C","E","G"],1,"saw")

	# syn1.playSignal(C)
	# syn1.playSignal(E)
	# syn1.playSignal(G)
	# syn1.playSignal(cMaj)

	# Super freakin' Mario
	first = syn1.genChord(["E5","F#/Gb4","B"],0.25,"saw")
	pause = syn1.genNote("",0.25,"saw")
	second = syn1.genChord(["F#/Gb4","C5","B"],0.25,"saw")
	third = syn1.genChord(["F#/Gb4","E5","B"],0.25,"saw")
	fourth = syn1.genChord(["G","B","G5"],0.25,"saw")
	threeFourthsPause = syn1.genNote("",0.75,"saw")
	fifth = syn1.genChord(["G","E3"],0.25,"saw")

	syn1.playSignal(first)
	syn1.playSignal(first)
	syn1.playSignal(pause)
	syn1.playSignal(first)
	syn1.playSignal(pause)
	syn1.playSignal(second)
	syn1.playSignal(third)
	syn1.playSignal(pause)
	syn1.playSignal(fourth)
	syn1.playSignal(threeFourthsPause)
	syn1.playSignal(fifth)

	syn1.visualize()


	# for note in Cmaj:
	# 	signal = syn1.genNote(note,0.5,"saw")
	# 	syn1.playSignal(signal)
	
	# syn1.genNote("D",0.25,"saw")
	# syn1.genNote("E",0.25,"saw")
	# syn1.genNote("C",0.25,"saw")
	# syn1.genNote("C",0.25,"saw")
	# syn1.genNote("D",0.25,"saw")
	# syn1.genNote("E",0.25,"saw")
	# syn1.genNote("C",0.25,"saw")
	# syn1.genNote("E",0.25,"saw")
	# syn1.genNote("F",0.25,"saw")
	# syn1.genNote("G",0.5,"saw")
	# syn1.genNote("E",0.25,"saw")
	# syn1.genNote("F",0.25,"saw")
	# syn1.genNote("G",0.5,"saw")

