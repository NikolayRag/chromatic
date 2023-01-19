import random



class ColorTools():
	def __init__(self):
		None



	def getColor(self):
		return(
			(random.randrange(255)/255., random.randrange(255)/255., random.randrange(255)/255.),
			(random.randrange(255)/255., random.randrange(255)/255., random.randrange(255)/255.),
		)
