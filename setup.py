#! /usr/local/bin/python3
import sys
from cx_Freeze import setup, Executable

setup(name='QUAD',
      version='0.1',
      description='Quadrant Time Management in a concise format',
      url='http://github.com/oakular/QuadGtk',
      author='Callum Warrilow',
      author_email='callum@oakular.com',
      license='GPLv2',
      iconfile='icons/quad.icns',
      packages=['quad'],
      executables = [Executable("quad/__init__.py")])
