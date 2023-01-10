from Args import *

from .AppWindow import *


class Ui():
	qApp = None

	appWindow = None

	trayIcon = None



	def initApp(self, _appName, _appIcon, _style):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create(_style))
		
		if _appIcon:
			self.qApp.setWindowIcon(QIcon(_appIcon))
		
		if _appName:
			self.qApp.setApplicationName(_appName)



	def initTray(self, _fileIcon):
		self.trayIcon = QSystemTrayIcon(QIcon(_fileIcon))

		self.trayIcon.show()



	def windowStart(self, _appWindow):
		self.appWindow = _appWindow


		screenWH = QApplication.primaryScreen().size()

		margin = screenWH *(1-Args.Application.wFactor) *.5
		cPos = Args.Application.wPos and QPoint(*Args.Application.wPos)
		cPos = cPos or ( QPoint(margin.width(), margin.height()) )

		cSize = Args.Application.wSize and QSize(*Args.Application.wSize)
		cSize = cSize or screenWH *Args.Application.wFactor


		self.appWindow.windowGeometry(cSize, cPos, Args.Application.wMaxi)

		self.appWindow.setCheckExit(Args.Cmdline.hold)



	def windowSave(self, _window):
		wSize = _window.windowGeometry()
		Args.Application.wSize = (wSize[0].width(), wSize[0].height())
		Args.Application.wPos = (wSize[1].x(), wSize[1].y())
		Args.Application.wMaxi = wSize[2]



##### PUBLIC



	def __init__(self, appName=None, fileIcon=None):
		self.initApp(appName, fileIcon, Args.Cmdline.style)


		if Args.Cmdline.tray:
			self.initTray(fileIcon)



	def setupWin(self, _window):
		self.windowStart(_window)
		self.trayIcon and self.trayIcon.activated.connect(self.appWindow.miniTray)

		return self.appWindow.setupWin


		
	def go(self):
		self.appWindow.show()

		self.qApp.exec_()

		self.windowSave(self.appWindow)


		logging.warning('Exiting')
