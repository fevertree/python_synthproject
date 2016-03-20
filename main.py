from Synth import Synth
import numpy as np

#sepapoisid

with Synth() as syn1:
	# syn1.visualize()
	# syn1.genNote("B",0.2,"sin")

	C = syn1.genNote("C",1,"sin")
	E = syn1.genNote("E",1,"sin")
	G = syn1.genNote("G",1,"sin")
	decodeddata1 = np.fromstring(C, np.int16)
	decodeddata2 = np.fromstring(E, np.int16)
	decodeddata3 = np.fromstring(G, np.int16)

	newdata = (decodeddata1 * 0.5 + decodeddata2* 0.5 + decodeddata3 * 0.5).astype(np.int16)
	syn1.playSignal(C)
	syn1.playSignal(E)
	syn1.playSignal(G)
	syn1.playSignal(newdata)
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

