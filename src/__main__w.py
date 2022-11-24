from os import path

import Ui
from Args import *


AppName = 'TemplatePySide2'


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
		'msg': ['pwned'],
	}
}


modulePath= path.abspath(path.dirname(__file__))
resUi = path.join(modulePath,'Ui/AppWindow.ui')
resIcon = path.join(modulePath,'Ui/icons/icon-app.svg')
resStyle = path.join(modulePath,'Ui/styles/default.qss')



if __name__ == '__main__':
	Args(AppPrefs, AppName, cmdlineBlock='Cmdline')

	Ui.Ui(AppName, resUi, resIcon, resStyle)
