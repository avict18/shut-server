# shutdown.spec
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all necessary modules for PIL and Tkinter
hiddenimports = collect_submodules('PIL') + collect_submodules('tkinter')

# Collect data files for PIL and Tkinter
datas = collect_data_files('PIL') + collect_data_files('tkinter') + [('logo.png', '.')]

a = Analysis(
    ['guitest.py'],  # Replace with your actual script filename
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="shutdown",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True if you want to see console output
    icon=None  # Add 'icon.ico' if needed
)
