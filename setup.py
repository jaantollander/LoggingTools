from setuptools import setup
from loggingtools import __version__

setup(
    name='LoggingTools',
    version=__version__,
    packages=['loggingtools', 'loggingtools.tests'],
    url='https://github.com/jaantollander/LoggingTools',
    license='MIT',
    author='Jaan Tollander de Balsch',
    author_email='jaan.tollander@gmail.com',
    description='Python logging dictionary configuration from yaml, json or Python dict'
)
