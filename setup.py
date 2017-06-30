# coding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import dplog


long_description = '''
        _       _             
     __| |_ __ | | ___   __ _ 
    / _` | '_ \| |/ _ \ / _` |
   | (_| | |_) | | (_) | (_| |
    \__,_| .__/|_|\___/ \__, |
         |_|            |___/ 
Write a nice log with a small amount of code
  Default:
    Log format:
      [levelName] ascTime filePath function lineNumber: message
    Color:
      [ERROR]   --> red
      [WARNING] --> yellow
      [INFO]    --> cyan
      [DEBUG]   --> green
    LOG_LEVEL = 10
      * 10 logging.DEBUG
      * 20 logging.INFO
      * 30 logging.WARNING|WARN
      * 40 logging.ERROR
      * 50 logging.CRITICAL|FATAL
'''

setup(
    name="dplog",
    version=dplog.__version__,
    author="doupeng",
    author_email="doupeng1993@sina.com",
    url="https://github.com/doupengs/dplog",
    py_modules=["dplog"],
    description="Pretty simple easy-to-use log",
    long_description=long_description,
    license="Apache License 2.0",
    platforms=["Linux"],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Intended Audience :: Developers",
        "License :: Apache License 2.0",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ]
)
