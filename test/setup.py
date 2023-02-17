from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('C:\\Users\\ghaith\\Desktop\\Artistic style project\\test1.py', base=base, target_name = 'test2')
]

setup(name='test1',
      version = '1',
      description = '[attt]',
      options = {'build_exe': build_options},
      executables = executables)
