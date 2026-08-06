import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--add-data=images;images',
    '--add-data=SQL;SQL',
    '-n=平阳新纪元学校夏季运动会管理系统',
    '-i=images\图标.ico',
    '-y',
])