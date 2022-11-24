# PySide2 template app suitable for bundling with PyInstall


##Features

* Automatically save/load settings within .INI file in user folder with Args singletone
* Auto save/load window Geometry and Maximize state
* Load from .UI template
* Apply .QSS stylesheet
* Set app name for caption
* Set .SVG app icon
* Commandline args supported:
	* `-tool=1` make window a draggable Tool (no standard frame and caption)
	* `-tray=1` allow to minimize to Tray
	* `-dnd=1` allow Drag-and-Drop onto app
	* `-hold=1` confirm at Exit
	* `-msg=string` apply provided string content

* Build with PyInstaller with `pyinstaller PyInst.TemplatePySide2.spec` provided config.



https://github.com/NikolayRag/TemplatePySide2
