import ytdownload.Application
import Pyinstaller.__main__

PyInstaller.__main__.run([
    'ytdownload.py',
    '--onefile',
    '--windowed'
])
