import pygame.midi



class DeviceMidiMX():
	devName = b'Arduino Micro'
	dev = None


	def __init__(self):
		pygame.midi.init()
		devsA = pygame.midi.get_count()
		for devN in range(devsA):
			devInfo = pygame.midi.get_device_info(devN)
			if not devInfo[3]:
				continue

			if devInfo[1] == self.devName:
				self.dev = pygame.midi.Output(devN)



	def setRGB(self, _black, _white):
		val = int((_white[0]+_black[0])/2*127)
		val = 0 if val<0 else val
		self.dev.write_short(0xB0, 0, val)

		val = int((_white[1]+_black[1])/2*127)
		val = 0 if val<0 else val
		self.dev.write_short(0xB0, 1, val)

		val = int((_white[2]+_black[2])/2*127)
		val = 0 if val<0 else val
		self.dev.write_short(0xB0, 2, val)



	def setRrrGggBbb(self, _rrr, _ggg, _bbb, _lift):
		self.setRGB((_rrr[0], _ggg[1], _bbb[2]), (_lift[0], _lift[1], _lift[2]))



	def relax(self):
		None
