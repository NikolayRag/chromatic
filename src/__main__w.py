from os import path

import Ui
from Args import *

from device.DeviceDisplay import *
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
		'tool': [0],
		'tray': [0],
		'dnd': [0],
		'hold': [0],
		'msg': ['chromatic'],
	}
}


modulePath= path.abspath(path.dirname(__file__))
resUi = path.join(modulePath,'Ui/AppWindow.ui')
resIcon = path.join(modulePath,'Ui/icons/icon-app.svg')
resStyle = path.join(modulePath,'Ui/styles/default.qss')



if __name__ == '__main__':
	Args(AppPrefs, AppName, cmdlineBlock='Cmdline')

	cDev = (
		DisplayMagnifix(),
		DeviceMidiMX(),
	)
	cTools = ColorTools()

	cUi = Ui.Ui(resUi, AppName, resIcon, resStyle)
	cUi.setup(cDev, cTools)
	cUi.go()

	for d in cDev:
		d.relax()
