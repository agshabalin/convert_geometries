from distutils.core import setup

setup(
    name='convert_geometries',
    version='0.1',
    packages=['convert_geometries',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=['scipy']
)
