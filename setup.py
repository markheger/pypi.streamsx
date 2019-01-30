from setuptools import setup
import streamsx._streams._version
setup(
  name = 'streamsx',
  packages = ['streamsx', 'streamsx.spl', 'streamsx.topology', 'streamsx.scripts', 'streamsx._streams'],
  include_package_data=True,
  version = streamsx._streams._version.__version__,
  description = 'IBM Streams Python Support',
  long_description = open('DESC.txt').read(),
  author = 'IBM Streams @ github.com',
  author_email = 'debrunne@us.ibm.com',
  license='Apache License - Version 2.0',
  url = 'https://github.com/IBMStreams/pypi.streamsx',
  keywords = ['streams', 'ibmstreams', 'streaming', 'analytics', 'streaming-analytics'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.6',
  ],
  install_requires=['requests', 'future', 'dill'],
  entry_points = {
        'console_scripts': [
            'streamsx-runner=streamsx.scripts.runner:main',
            'streams-service=streamsx.scripts.service:main',
            'streamsx-info=streamsx.scripts.info:main',
            'spl-python-extract=streamsx.scripts.extract:main'
        ],
  },
)
