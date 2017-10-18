from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='panda3d_inputmapper',
    version='0.1',
    description='Simple input mapper to use with Panda3D',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='panda3d gamedev',
    url='https://github.com/Moguri/panda3d_inputmapper',
    author='Mitchell Stokes',
    license='BSD',
    packages=['inputmapper'],
)
