# -*- mode: python ; coding: utf-8 -*-
import shutil, os

block_cipher = None


a = Analysis(['run.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='AnnouncementsWindow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon='Data\\favicon.ico')

os.makedirs('dist/Data')
shutil.copyfile('Data/favicon.ico', 'dist/Data/favicon.ico')
shutil.copyfile('filters.txt', 'dist/filters.txt')
shutil.copyfile('wordcolor.txt', 'dist/wordcolor.txt')
shutil.copyfile('Data/filters.dat', 'dist/Data/filters.dat')
shutil.copyfile('readme.md', 'dist/readme.md')
shutil.copyfile('readme.txt', 'dist/readme.txt')
shutil.copytree('Icons', 'dist/Icons')
shutil.copyfile('icon.cfg', 'dist/icon.cfg')

