import logging


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

from .BindFilter import *



class AppWindow(QObject):
	mouseGrabOffset= None


	#support for window size/pos while maximized issue
	rtSize = [None, None]
	rtPos = [None, None]


	wMain = None
	wCaption = None
	wContent = None


	flagCheckExit = True



	def ynBox(self, _txt, _txtQ, btnYes, btnNo, yesno=False):
		msgBox = QMessageBox()
		msgBox.setText(_txt)
		msgBox.setInformativeText(_txtQ)
		msgBox.setStandardButtons(btnYes | btnNo)
		msgBox.setDefaultButton(btnNo)
		if msgBox.exec() == (btnYes if yesno else btnNo):
			return True



########## -support



#specific logic relying on QT events order
# for (re)storing "true" window size/pos while maximized
	def moved(self, _e):
		if self.rtPos[1] != None:
			self.rtPos[0] = self.rtPos[1]
			self.rtPos[1] = self.wMain.pos()
		else:
			self.rtPos[1] = self.rtPos[0]



	def resized(self, _e):
		if self.rtSize[1] != None:
			self.rtSize[0] = self.rtSize[1]
			self.rtSize[1] = self.wMain.size()
		else:
			self.rtSize[1] = self.rtSize[0]


	def maximized(self, _e):
		if self.wMain.isMaximized():
			self.rtSize[1] = self.rtSize[0]
			self.rtPos[1] = self.rtPos[0]



	def tryExit(self, event):
		if not self.flagCheckExit:
			return


		if self.ynBox("Out", "Maybe not?", QMessageBox.Ok, QMessageBox.Cancel):
			event.ignore()

		if event.isAccepted():
			logging.warning('left')
		else:
			logging.warning('stay')


		return True



	def dropped(self, _e):
		logging.warning(_e.mimeData().urls())



#toolwindow mouse drag support
	def mouseGrab(self, _offset=None):
		self.mouseGrabOffset = None

		if _offset:
			self.mouseGrabOffset = _offset - self.wMain.pos()



######### PUBLIC



	def __init__(self, fileUi, fileStyle=None, isTray=False, isTool=False, isDnd=False):
		QObject.__init__(self)


		cMain = self.wMain = QUiLoader().load(fileUi)
		if fileStyle:
			self.setStyle(fileStyle)


		BindFilter({
				QEvent.Close: self.tryExit,
				QEvent.Move: self.moved,
				QEvent.Resize: self.resized,
				QEvent.WindowStateChange: self.maximized,
			},
			cMain
		)


		#capture widgets
		self.wCaption= cMain.findChild(QWidget, "frameCaption")

		self.wContent= cMain.findChild(QWidget, "labContent")

		

		if isTool:
			logging.warning('Tool mode')

			cMain.setWindowFlags(Qt.FramelessWindowHint)

			BindFilter({
					QEvent.MouseButtonPress: lambda e: self.mouseGrab(e.globalPos()),
					QEvent.MouseButtonRelease: lambda e: self.mouseGrab(),
					QEvent.MouseMove: lambda e: self.mouseGrabOffset and self.wMain.move(e.globalPos()-self.mouseGrabOffset)
			 	},
			 	cMain
		 	)

		else:
		 	self.wCaption.hide()



		if isTray: #override minimize
			BindFilter({
					QEvent.WindowStateChange: lambda e: self.miniTray(),
			 	},
			 	cMain
			 )



		if isDnd:
			logging.warning('Dnd on')

			BindFilter({
					QEvent.DragEnter: lambda e: e.acceptProposedAction(),
					QEvent.Drop: self.dropped,
			 	},
			 	cMain
		 	)



	def show(self):
		self.wMain.show()


	def close(self):
		isVis = self.wMain.isVisible()
		self.wMain.show() #not to play with setQuitOnLastWindowClosed

		self.wMain.close()

		self.wMain.setVisible(isVis)

	


	#slot for tray minimize/restore only
	def miniTray(self, _reason=None):
		if _reason == None and self.wMain.isMinimized():
			logging.warning('to tray')

			QTimer.singleShot(0, self.wMain.hide)


		if _reason == QSystemTrayIcon.Trigger:
			logging.warning('from tray')

			self.show()
			self.wMain.showNormal()



	def setStyle(self, _fileStyle):
		with open(_fileStyle) as fQss:
			self.wMain.setStyleSheet(fQss.read())



	def setCheckExit(self, _state):
		self.flagCheckExit = _state



	def setupWin(self, _content):
		self.wContent.setText(_content)



	def windowGeometry(self, _size=None, _pos=None, maximize=None):
		if _size!=None and _pos!=None:
			self.wMain.resize( _size )

			self.wMain.move( _pos )

			if maximize:
				self.wMain.showMaximized()

			#marker values to pass to following events
			self.rtSize = [_size,None]
			self.rtPos = [_pos,None]


		return [self.rtSize[1], self.rtPos[1], self.wMain.isMaximized()]
