# -*- mode: python ; coding: utf-8 -*-

# Pyinstaller one-file spec script for building OpenTimelineIO app packages.
# Igor Ridanovic. igor at hdhead. com

block_cipher = None

# OTIO files that are ignored by the Pyinstaller's search
otiodatas=[
    (
        '/Users/igor/.pyenv/versions/2.7.18/lib/python2.7/site-packages/opentimelineio',
        'opentimelineio'
        ),
   (
        '/Users/igor/.pyenv/versions/2.7.18/lib/python2.7/site-packages/opentimelineio_contrib',
        'opentimelineio_contrib'
        )
    ]

# Modules that are ignored by the Pyinstaller's search
hImports = ['numbers', 'fractions', 'xml.dom', 'colorsys', 'aaf2']
 
pExec   = ['/Users/igor/sbin/MyPythonApp']  # The Py app top level directory
main    = ['MyPythonApp.py']  # The main Py app file
appName = 'MyPythonApp'  # The name for the packaged build


a = Analysis(main,
             pathex=pExec,
             binaries=[],
             datas=otiodatas,
             hiddenimports=hImports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=appName,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
