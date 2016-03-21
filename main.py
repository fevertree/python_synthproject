from Synth import Synth
import numpy as np
from Music import Music

#sepapoisid

m = Music()

Cmaj = m.returnMajorScale("C",4)

with Synth(60.0) as syn1:
	# syn1.visualize()

	C = syn1.genNote("C",0.25,"saw")
	E = syn1.genNote("E",0.25,"saw")
	G = syn1.genNote("G",0.25,"saw")
	cMaj = syn1.genChord(["C","E","G"],1,"saw")

	syn1.playSignal(C)
	syn1.playSignal(E)
	syn1.playSignal(G)
	syn1.playSignal(cMaj)

	# for note in Cmaj:
	# 	signal = syn1.genNote(note,0.3,"saw")
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

