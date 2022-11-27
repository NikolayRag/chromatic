from ctypes import *



class DisplayMagnifix():
	magnification_api = CDLL('magnification.dll')

	setup = False



	def __init__(self):
		None



	def setRGB(self, _black, _white):
		self.setRrrGggBbb(
			(_white[0]-_black[0], 0, 0),
			(0, _white[1]-_black[1], 0),
			(0, 0, _white[2]-_black[2]),
			(_black[0], _black[1], _black[2])
		)



	def setRrrGggBbb(self, _rrr, _ggg, _bbb, _lift):
		if not self.setup:
			self.setup = True

			self.magnification_api.MagInitialize()



		self.magnification_api.MagSetFullscreenColorEffect((c_float *25)(
			_rrr[0], _rrr[1], _rrr[2], 0, 0,
			_ggg[0], _ggg[1], _ggg[2], 0, 0,
			_bbb[0], _bbb[1], _bbb[2], 0, 0,
			0, 0, 0, 1, 0,
			_lift[0], _lift[1], _lift[2], 0, 1
		))



	def relax(self):
		self.magnification_api.MagUninitialize()

		self.setup = False
