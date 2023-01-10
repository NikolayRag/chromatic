from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Uiui



class ChromaticWin(Uiui.AppWindow):
	wButton = None

	wSliderRr = wSliderRg = wSliderRb = None
	wSliderGr = wSliderGg = wSliderGb = None
	wSliderBr = wSliderBg = wSliderBb = None
	wSliderLr = wSliderLg = wSliderLb = None



	def setupWin(self, tool1, tool2):
		self.wButton= self.wMain.findChild(QPushButton, "btnColor")

		self.wSliderRr= self.wMain.findChild(QSlider, "sliderRr")
		self.wSliderRg= self.wMain.findChild(QSlider, "sliderRg")
		self.wSliderRb= self.wMain.findChild(QSlider, "sliderRb")
		self.wSliderGr= self.wMain.findChild(QSlider, "sliderGr")
		self.wSliderGg= self.wMain.findChild(QSlider, "sliderGg")
		self.wSliderGb= self.wMain.findChild(QSlider, "sliderGb")
		self.wSliderBr= self.wMain.findChild(QSlider, "sliderBr")
		self.wSliderBg= self.wMain.findChild(QSlider, "sliderBg")
		self.wSliderBb= self.wMain.findChild(QSlider, "sliderBb")

		self.wSliderLr= self.wMain.findChild(QSlider, "sliderLr")
		self.wSliderLg= self.wMain.findChild(QSlider, "sliderLg")
		self.wSliderLb= self.wMain.findChild(QSlider, "sliderLb")


		def sliderSet():
			rgbRGB = tool1()

			self.wSliderRr.setValue(rgbRGB[1][0]*255-rgbRGB[0][0]*255)
			self.wSliderRg.setValue(0)
			self.wSliderRb.setValue(0)
			self.wSliderGr.setValue(0)
			self.wSliderGg.setValue(rgbRGB[1][1]*255-rgbRGB[0][1]*255)
			self.wSliderGb.setValue(0)
			self.wSliderBr.setValue(0)
			self.wSliderBg.setValue(0)
			self.wSliderBb.setValue(rgbRGB[1][2]*255-rgbRGB[0][2]*255)
			self.wSliderLr.setValue(rgbRGB[0][0]*255)
			self.wSliderLg.setValue(rgbRGB[0][1]*255)
			self.wSliderLb.setValue(rgbRGB[0][2]*255)

		self.wButton.pressed.connect(sliderSet)


		def sliderMatrix():
			for cTool in tool2:
				cTool(
					(self.wSliderRr.value()/255., self.wSliderRg.value()/255., self.wSliderRb.value()/255.),
					(self.wSliderGr.value()/255., self.wSliderGg.value()/255., self.wSliderGb.value()/255.),
					(self.wSliderBr.value()/255., self.wSliderBg.value()/255., self.wSliderBb.value()/255.),
					(self.wSliderLr.value()/255., self.wSliderLg.value()/255., self.wSliderLb.value()/255.)
				)
		
		sliderMatrix()


		self.wSliderRr.valueChanged.connect(sliderMatrix)
		self.wSliderRg.valueChanged.connect(sliderMatrix)
		self.wSliderRb.valueChanged.connect(sliderMatrix)
		self.wSliderGr.valueChanged.connect(sliderMatrix)
		self.wSliderGg.valueChanged.connect(sliderMatrix)
		self.wSliderGb.valueChanged.connect(sliderMatrix)
		self.wSliderBr.valueChanged.connect(sliderMatrix)
		self.wSliderBg.valueChanged.connect(sliderMatrix)
		self.wSliderBb.valueChanged.connect(sliderMatrix)
		self.wSliderLr.valueChanged.connect(sliderMatrix)
		self.wSliderLg.valueChanged.connect(sliderMatrix)
		self.wSliderLb.valueChanged.connect(sliderMatrix)
