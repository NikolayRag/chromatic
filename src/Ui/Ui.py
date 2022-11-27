from Args import *

from .AppWindow import *


class Ui():
	qApp = None

	appWin = None

	trayIcon = None



	def initApp(self, _appName, _appIcon):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('fusion'))
		
		if _appIcon:
			self.qApp.setWindowIcon(QIcon(_appIcon))
		
		if _appName:
			self.qApp.setApplicationName(_appName)



	def initTray(self, _fileIcon):
		self.trayIcon = QSystemTrayIcon(QIcon(_fileIcon))

		self.trayIcon.show()



	def windowStart(self, _fileUi, _fileStyle):
		screenWH = QApplication.primaryScreen().size()

		margin = screenWH *(1-Args.Application.wFactor) *.5
		cPos = Args.Application.wPos and QPoint(*Args.Application.wPos)
		cPos = cPos or ( QPoint(margin.width(), margin.height()) )

		cSize = Args.Application.wSize and QSize(*Args.Application.wSize)
		cSize = cSize or screenWH *Args.Application.wFactor


		appWindow = AppWindow(
			_fileUi,
			fileStyle=_fileStyle,
			isTool=Args.Cmdline.tool,
			isTray=Args.Cmdline.tray,
			isDnd=Args.Cmdline.dnd
		)
		appWindow.windowGeometry(cSize, cPos, Args.Application.wMaxi)

		appWindow.setCheckExit(Args.Cmdline.hold)


		return appWindow



	def windowSave(self, _window):
		wSize = _window.windowGeometry()
		Args.Application.wSize = (wSize[0].width(), wSize[0].height())
		Args.Application.wPos = (wSize[1].x(), wSize[1].y())
		Args.Application.wMaxi = wSize[2]



	def __init__(self, _resUi, appName=None, fileIcon=None, fileStyle=None):
		self.initApp(appName, fileIcon)


		self.appWin = self.windowStart(_resUi, fileStyle)

		if Args.Cmdline.tray:
			self.initTray(fileIcon)

			self.trayIcon.activated.connect(self.appWin.miniTray)



	def setup(self, _content):
		self.appWin.setContent(_content)



	def go(self):
		self.appWin.show()

		self.qApp.exec_()

		self.windowSave(self.appWin)


		logging.warning('Exiting')
