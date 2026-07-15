# calculatrice.spec
# PyInstaller spec file for calculatrice.py

from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(
    ['calculatrice.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Collect Qt resources (for PySide6)
datas = collect_data_files('pyside6')

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exec_flags = []
if 'win' in sys.platform:
    exec_flags.append('--windowed')  # No console window
    exec_flags.append('--onefile')   # Single .exe file
    exec_flags.append('--name=calculatrice')
    exec_flags.append('--icon=styles/yes.png')  # Chemin vers ton icône (à adapter)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas + datas,
    [],
    name='calculatrice',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console (GUI app)
    icon='styles/yes.png',  # Chemin vers ton icône
)
