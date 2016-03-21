from Synth import Synth
import numpy as np

#sepapoisid

with Synth() as syn1:
	# syn1.visualize()
	# syn1.genNote("B",0.2,"sin")

	C = syn1.genNote("C",1,"saw")
	E = syn1.genNote("E",1,"saw")
	G = syn1.genNote("G",1,"saw")
	cMaj = syn1.genChord(["C","E","G"],1.5,"saw")

	syn1.playSignal(C)
	syn1.playSignal(E)
	syn1.playSignal(G)
	syn1.playSignal(cMaj)

	
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

