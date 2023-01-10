from os import path

import Uiui
from Args import *


from Ui.ChromaticWin import *

from device.DeviceMagnifix import *
from device.DeviceMidiMX import *
from tools.ColorTools import *



AppName = 'chromatic'


AppPrefs = {
	'Application': {
		'wFactor': [.8],
		'wSize': [None],
		'wPos': [None],
		'wMaxi': [False],
	},
	'Cmdline': {
		'tray': [False],
		'hold': [False],
		'style': ['fusion'],
	}
}


modulePath= path.abspath(path.dirname(__file__))
resUi = path.join(modulePath,'Ui/AppWindow.ui')
resIcon = path.join(modulePath,'Ui/icons/icon-app.svg')
resStyle = path.join(modulePath,'Ui/styles/default.qss')



if __name__ == '__main__':
	Args(AppPrefs, AppName, cmdlineBlock='Cmdline')

	cDev = (
		DeviceMagnifix(),
		DeviceMidiMX(),
	)
	cTools = ColorTools()

	cUi = Uiui.Ui(AppName, resIcon)
	appWindow = ChromaticWin(
		resUi,
		fileStyle=resStyle,
		isTray=Args.Cmdline.tray,
	)
	cUi.setupWin(appWindow)(
		tool1=cTools.getColor,
		tool2=list(dev.setRrrGggBbb for dev in cDev)
	)

	cUi.go()

	for d in cDev:
		d.relax()
