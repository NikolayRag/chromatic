from Args import *

from .AppWindow import *


class Ui():
	resUi = None
	resIcon = None
	resStyle = None


	qApp = None

	trayIcon = None



	def initApp(self, _appName):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('fusion'))
		self.qApp.setWindowIcon(QIcon(self.resIcon))
		if _appName:
			self.qApp.setApplicationName(_appName)



	def initTray(self):
		self.trayIcon = QSystemTrayIcon(QIcon(self.resIcon))

		self.trayIcon.show()



	def windowStart(self):
		screenWH = QApplication.primaryScreen().size()

		margin = screenWH *(1-Args.Application.wFactor) *.5
		cPos = Args.Application.wPos and QPoint(*Args.Application.wPos)
		cPos = cPos or ( QPoint(margin.width(), margin.height()) )

		cSize = Args.Application.wSize and QSize(*Args.Application.wSize)
		cSize = cSize or screenWH *Args.Application.wFactor


		appWindow = AppWindow(
			self.resUi,
			resStyle=self.resStyle,
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



	def __init__(self, appName=None, resUi=None, resIcon=None, resStyle=None):
		self.resUi = resUi
		self.resIcon = resIcon
		self.resStyle = resStyle

		self.initApp(appName)


		appWin = self.windowStart()
		if Args.Cmdline.tray:
			self.initTray()

			self.trayIcon.activated.connect(appWin.miniTray)


		appWin.setContent(Args.Cmdline.msg)

		appWin.show()

		self.qApp.exec_()

		self.windowSave(appWin)


		logging.warning('Exiting')
