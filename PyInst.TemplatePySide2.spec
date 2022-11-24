# -*- mode: python -*-

block_cipher = None


a = Analysis(['src/__main__w.py'],
	pathex=[''],
	binaries=None,
	datas=[
		('src/Ui/AppWindow.ui', 'Ui'),
		('src/Ui/icons/icon-app.svg', 'Ui/icons'),
		('src/Ui/styles/default.qss', 'Ui/styles'),
#		('bin/bin.exe','src/bin/bin.exe','DATA'),
	],
	hiddenimports=['PySide2.QtXml'],
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='TemplatePySide2',
          debug=False,
          strip=False,
          upx=True,
          console=False )
 