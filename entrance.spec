# -*- mode: python -*-

block_cipher = None


a = Analysis(['entrance.py'],
             pathex=['/Users/mapzchen/myShell/qtPro/fastColuaco'],
             binaries=None,
             datas=None,
             hiddenimports=[],
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
          [('/data/settings.png','/Users/mapzchen/myShell/qtPro/fastColuaco/data/settings.png','DATA')],
          [('/data/ver.png','/Users/mapzchen/myShell/qtPro/fastColuaco/data/ver.png','DATA')],
          [('/data/items.conf','/Users/mapzchen/myShell/qtPro/fastColuaco/data/items.conf','DATA')],
          [('/data/generalConfig.conf','/Users/mapzchen/myShell/qtPro/fastColuaco/data/generalConfig.conf','DATA')],
          name='210打包上传工具',
          debug=False,
          strip=False,
          upx=True,
          console=False, 
          icon='Icon-72.ico')
